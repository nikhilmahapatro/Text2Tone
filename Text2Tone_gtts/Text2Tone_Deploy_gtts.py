
#-----------------------------------------TEXT2TONE----------------------------------------#

import streamlit as st
from gtts import gTTS
import io

st.title("Text2Tone")
st.write("Enter text below and hear it spoken aloud.")

text = st.text_area("Your text here:", height=250)

if st.button("Speak"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        tts = gTTS(text, lang='en')
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        st.audio(audio_bytes, format='audio/mp3')