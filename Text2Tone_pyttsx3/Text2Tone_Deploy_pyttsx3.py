
#-----------------------------------------TEXT2TONE----------------------------------------#

import streamlit as st
import pyttsx3
import os
import time

def save_tts(text, filename='output.mp3'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename

st.title("Text2Tone (Offline Mode)")
st.write("This version uses your system's built-in voice engine (pyttsx3).")

text = st.text_area("Enter your text below:", height=250)

if st.button("Generate Voice"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        filepath = save_tts(text)
        st.audio(filepath, format='audio/mp3')

        # Wait a moment to ensure Streamlit grabs the file
        time.sleep(1)

        # Clean up
        try:
            os.remove(filepath)
        except Exception as e:
            st.error(f"Failed to delete temp file: {e}")