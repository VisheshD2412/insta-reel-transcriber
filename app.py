import streamlit as st
import yt_dlp
import os
import shutil
import tempfile
import time
from pathlib import Path
from faster_whisper import WhisperModel

# Configuration
DOWNLOAD_DIR = "downloads"
MAX_FILE_AGE_HOURS = 1  # Delete files older than 1 hour
MAX_DOWNLOAD_FILES = 10  # Keep maximum 10 files at a time

# Create downloads directory if it doesn't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Instagram Reel Transcript Tool")
st.title("Instagram Reel Transcript Generator")

url = st.text_input("Paste Instagram Reel URL")

@st.cache_resource
def load_model():
    return WhisperModel("base")

def cleanup_old_files():
    """Delete old downloaded files to prevent disk bloat"""
    downloads_path = Path(DOWNLOAD_DIR)
    if not downloads_path.exists():
        return
    
    # Delete files older than MAX_FILE_AGE_HOURS
    current_time = time.time()
    files_deleted = 0
    
    for file_path in downloads_path.glob("*.mp4"):
        file_age = current_time - file_path.stat().st_mtime
        if file_age > (MAX_FILE_AGE_HOURS * 3600):
            try:
                file_path.unlink()
                files_deleted += 1
            except Exception as e:
                print(f"Could not delete {file_path}: {e}")
    
    # If still too many files, delete oldest ones
    files = sorted(downloads_path.glob("*.mp4"), key=lambda f: f.stat().st_mtime)
    while len(files) > MAX_DOWNLOAD_FILES:
        try:
            files[0].unlink()
            files.pop(0)
        except Exception as e:
            print(f"Could not delete {files[0]}: {e}")
    
    if files_deleted > 0:
        st.caption(f"🧹 Cleaned up {files_deleted} old file(s)")

def get_unique_filename():
    """Generate a unique filename with timestamp"""
    timestamp = int(time.time())
    return f"{DOWNLOAD_DIR}/reel_{timestamp}.mp4"

def download_reel(url):
    """Download reel and return file path"""
    ydl_opts = {
        "outtmpl": get_unique_filename(),
        "format": "best",
        "quiet": True,
        "no_warnings": True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

if st.button("Transcribe"):
    if not url:
        st.warning("Paste a reel link first")
    else:
        video_path = None
        try:
            # Clean up old files before downloading new one
            cleanup_old_files()
            
            with st.spinner("📥 Downloading reel..."):
                video_path = download_reel(url)
            
            with st.spinner("🤖 Loading transcription model..."):
                model = load_model()
            
            with st.spinner("✍️ Transcribing audio..."):
                segments, _ = model.transcribe(video_path)
                transcript = " ".join(segment.text for segment in segments)
            
            # Display success and transcript
            st.success("✅ Transcription complete!")
            st.text_area("📝 Transcript", transcript, height=300)
            
            # Show file info for transparency
            file_size = os.path.getsize(video_path) / (1024 * 1024)  # Convert to MB
            st.caption(f"📁 Processed: {file_size:.1f} MB")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
        
        finally:
            # Delete this specific file immediately after processing
            if video_path and os.path.exists(video_path):
                try:
                    os.unlink(video_path)
                    st.caption("🗑️ Temporary file deleted immediately")
                except Exception as e:
                    print(f"Could not delete {video_path}: {e}")

# Add a manual cleanup button in sidebar
st.sidebar.title("Storage Management")
if st.sidebar.button("🗑️ Clean Downloads Now"):
    try:
        downloads_path = Path(DOWNLOAD_DIR)
        if downloads_path.exists():
            files = list(downloads_path.glob("*.mp4"))
            for file in files:
                file.unlink()
            st.sidebar.success(f"Deleted {len(files)} file(s)")
        else:
            st.sidebar.info("No downloads folder found")
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")

# Show current storage usage
if st.sidebar.checkbox("Show Storage Info"):
    downloads_path = Path(DOWNLOAD_DIR)
    if downloads_path.exists():
        files = list(downloads_path.glob("*.mp4"))
        total_size = sum(f.stat().st_size for f in files) / (1024 * 1024)
        st.sidebar.write(f"📁 Files: {len(files)}")
        st.sidebar.write(f"💾 Total size: {total_size:.2f} MB")
        
        if files:
            with st.sidebar.expander("View files"):
                for f in files:
                    age_minutes = (time.time() - f.stat().st_mtime) / 60
                    st.write(f"- {f.name} ({age_minutes:.0f} min old)")
    else:
        st.sidebar.write("No downloads folder yet")

st.sidebar.markdown("---")
st.sidebar.caption("""
**Cleanup settings:**
- Files deleted immediately after transcription
- Manual cleanup button available above
""")