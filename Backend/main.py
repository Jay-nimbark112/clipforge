from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import requests
import subprocess

app = FastAPI()

# Allow CORS for your Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Output folder
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Serve output folder as static files
app.mount("/output", StaticFiles(directory=OUTPUT_DIR), name="output")

class MediaRequest(BaseModel):
    url: str
    operation: str  # "thumbnail", "compress", "extract_audio"

@app.post("/process")
def process_media(req: MediaRequest):
    input_url = req.url
    operation = req.operation

    # Extract filename safely
    filename = os.path.basename(input_url.split("?")[0])
    local_input = os.path.join(OUTPUT_DIR, f"input_{filename}")

    # Download video first
    try:
        r = requests.get(input_url, stream=True)
        if r.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to download file")
        with open(local_input, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download error: {e}")

    # Process file
    try:
        output_file = os.path.join(OUTPUT_DIR, f"{operation}_{filename}")

        if operation == "thumbnail":
            output_file += ".jpg"
            # Generate thumbnail at 0.5s
            subprocess.run([
                "ffmpeg", "-y", "-i", local_input,
                "-ss", "00:00:00.5", "-frames:v", "1", "-q:v", "2",
                output_file
            ], check=True)

        elif operation == "compress":
            output_file += ".mp4"
            subprocess.run([
                "ffmpeg", "-y", "-i", local_input,
                "-vcodec", "libx264", "-crf", "28", output_file
            ], check=True)

        elif operation == "extract_audio":
            output_file += ".mp3"
            subprocess.run([
                "ffmpeg", "-y", "-i", local_input,
                "-q:a", "0", "-map", "a", output_file
            ], check=True)
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")

        # Return URL for React frontend
        return {"status": "success", "output": f"/output/{os.path.basename(output_file)}"}

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"FFmpeg error: {e}")