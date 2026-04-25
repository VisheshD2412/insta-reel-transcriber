import streamlit as st
import yt_dlp
import os
from faster_whisper import WhisperModel

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Instagram Reel Transcript Tool")
st.title("Instagram Reel Transcript Generator")

url = st.text_input("Paste Instagram Reel URL")

@st.cache_resource
def load_model():
    return WhisperModel("base")

if st.button("Transcribe"):
    if not url:
        st.warning("Paste a reel link first")
    else:
        try:
            with st.spinner("Downloading reel..."):
                ydl_opts = {
                    "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",
                    "format": "best"
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    video_path = ydl.prepare_filename(info)

            with st.spinner("Loading model..."):
                model = load_model()

            with st.spinner("Transcribing..."):
                segments, _ = model.transcribe(video_path)

                transcript = ""
                for segment in segments:
                    transcript += segment.text + " "

            st.success("Done!")
            st.text_area("Transcript", transcript, height=300)

        except Exception as e:
            st.error(f"Error: {str(e)}")