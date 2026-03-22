# ClipForge 🎬

ClipForge is a **full-stack web application** for processing videos directly from a URL.  
It supports **thumbnail generation, audio extraction, and video compression** using a FastAPI backend and a React frontend.

---

## 📂 Project Structure

project2/
├─ frontend/ # React frontend application
├─ backend/ # FastAPI backend application
└─ .gitignore



---

## ⚙️ Technologies Used

### Backend
- **Python 3.10+**
- **FastAPI** for API endpoints
- **FFmpeg** for video/audio processing
- **Pydantic** for request validation
- **Requests** for downloading videos
- **UUID** for unique file naming

### Frontend
- **React.js** with functional components
- **Axios** for API requests
- **CSS** for styling

---

## 🎯 How to Use ClipForge

Follow these steps to process videos using ClipForge:

1. **Open the App**  
   Open your browser and navigate to:  
   `http://localhost:3000` (after starting frontend and backend).

2. **Paste a Video URL**  
   - Enter a direct video URL in the input box.  
   - Example: `https://placeholdervideo.dev/1280x720`  
   - Make sure the URL is correct. If the URL is invalid or inaccessible, an error message will appear.

3. **Select an Operation**  
   Choose **one** operation from the dropdown menu:
   - **Thumbnail** – generate a video thumbnail image.  
   - **Compress Video** – reduce the video file size while maintaining quality.  
   - **Extract Audio** – extract the audio from the video as MP3.

4. **Process the Video**  
   - Click the **Process** button.  
   - Wait a few seconds while the backend processes the video.  
   - During processing, the button shows **“Processing…”**.

5. **View and Download Result**  
   - Once processing is complete, the result appears:
     - **Thumbnail** → image preview  
     - **Compress Video** → video player  
     - **Extract Audio** → audio player  
   - Click **📥 Download** to save the file to your device.

6. **Reset the Form**  
   - Click the **Reset** button to clear the input and result.  
   - You can then paste a new URL and repeat the process.

7. **Error Handling**  
   - If the URL is invalid or cannot be accessed, an error message will be displayed below the input box.  
   - Make sure to provide a valid, publicly accessible video URL.

---

### ✅ Example Video URLs for Testing

- `https://placeholdervideo.dev/1280x720`  
- `https://placeholdervideo.dev/1920x1080`




## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Jay-nimbark112/clipforge.git
cd clipforge


cd backend
pip install -r requirements.txt
# Make sure FFmpeg is installed and accessible in your PATH
uvicorn main:app --reload

cd frontend
npm install
npm start



Features
Thumbnail Extraction
Generate a thumbnail image from a video at 1 second timestamp.
Audio Extraction
Extract audio (MP3) from any video URL.
Video Compression
Compress video to reduce file size while maintaining quality.
Direct URL Support
Works with publicly accessible video URLs (MP4, MOV, etc.).
Download Results
Download processed videos, audio, or thumbnails directly from the UI.
