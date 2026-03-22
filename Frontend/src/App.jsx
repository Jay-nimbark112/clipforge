import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [operation, setOperation] = useState("thumbnail");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleReset = () => {
    setUrl("");
    setOperation("thumbnail");
    setResult(null);
    setError("");
  };

  const handleProcess = async () => {
    setError("");
    if (!url.trim()) {
      setError("Please enter a URL");
      return;
    }

    // URL VALIDATION (Invalid URL Check)
    const urlPattern = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$/;
    if (!urlPattern.test(url)) {
      setError("Invalid URL format. Please paste a direct link (https://...)");
      return;
    }

    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/process", { url, operation });
      setResult({ url: `http://127.0.0.1:8000${res.data.output}`, type: operation });
    } catch (err) {
      setError(err.response?.data?.detail || "Connection failed. Try a different link.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>ClipForge 🎬</h1>
      <div className="card">
        <input type="text" placeholder="Enter video URL..." value={url} onChange={(e) => setUrl(e.target.value)} />
        <select value={operation} onChange={(e) => setOperation(e.target.value)}>
          <option value="thumbnail">Thumbnail</option>
          <option value="compress">Compress Video</option>
          <option value="extract_audio">Extract Audio</option>
        </select>
        <div className="button-group">
          <button className="process-btn" onClick={handleProcess} disabled={loading}>{loading ? "Processing..." : "Process"}</button>
          <button className="reset-btn" onClick={handleReset}>Reset</button>
        </div>
        {error && <p className="error-message">{error}</p>}
      </div>

      {result && (
        <div className="result-area">
          <h3>Result Ready:</h3>
          {result.type === "thumbnail" && <img src={result.url} alt="res" />}
          {result.type === "compress" && <video key={result.url} controls src={result.url} width="100%" />}
          {result.type === "extract_audio" && <audio key={result.url} controls src={result.url} style={{width:"100%"}} />}
          <br /><a href={result.url} download className="download-link">📥 Download</a>
        </div>
      )}
    </div>
  );
}
export default App;