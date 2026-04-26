import streamlit as st
import yt_dlp
import os
import time
from pathlib import Path
import whisper  # ✅ Changed from faster_whisper

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Instagram Reel Transcript Tool")
st.title("Instagram Reel Transcript Generator")

url = st.text_input("Paste Instagram Reel URL")

@st.cache_resource
def load_model():
    return whisper.load_model("base")  # ✅ Changed

def get_unique_filename():
    timestamp = int(time.time())
    return f"{DOWNLOAD_DIR}/reel_{timestamp}.mp4"

def download_reel(url):
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
            with st.spinner("📥 Downloading reel..."):
                video_path = download_reel(url)
            
            with st.spinner("🤖 Loading model..."):
                model = load_model()
            
            with st.spinner("✍️ Transcribing..."):
                result = model.transcribe(video_path)  # ✅ Changed
                transcript = result["text"]  # ✅ Changed
            
            st.success("✅ Complete!")
            st.text_area("Transcript", transcript, height=300)
            
            file_size = os.path.getsize(video_path) / (1024 * 1024)
            st.caption(f"📁 Processed: {file_size:.1f} MB")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
        
        finally:
            if video_path and os.path.exists(video_path):
                try:
                    os.unlink(video_path)
                    st.caption("🗑️ Deleted")
                except Exception as e:
                    print(f"Could not delete: {e}")