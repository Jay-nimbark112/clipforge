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
