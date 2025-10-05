import os
import requests
import streamlit as st

NASA_API_KEY = os.getenv("NASA_API_KEY", "tQ9mfp3AgyuiCfWCnvdTMBTd58J1fdWg3D2lm1Af")

def get_nasa_image():
    try:
        res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}", timeout=10)
        data = res.json()
        media_type = data.get("media_type", "image")
        img = data.get("hdurl") if media_type == "image" else data.get("thumbnail_url")
        return img, data.get("title", "NASA Image of the Day"), data.get("explanation", "No description.")
    except Exception:
        return None, "Error", "Could not load NASA image."

def render_nasa_image():
    st.header("🌌 NASA Space Imagery")
    img, title, explanation = get_nasa_image()
    if img:
        st.image(img, caption=title, use_container_width=True)
        with st.expander("Description"):
            st.write(explanation)
    else:
        st.warning("No image available.")
