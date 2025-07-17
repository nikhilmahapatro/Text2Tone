# Text2Tone

Text2Tone is a minimal text-to-speech demo that converts user input into spoken audio using two different engines:

- **gTTS (Google Text-to-Speech)** for realistic, natural-sounding voices (requires internet)
- **pyttsx3** for offline voice synthesis using your system's built-in speech engine

The frontend is available in:
- **Streamlit** for a clean, simple web app

---

## What's included

- `app_streamlit_gtts.py` – Streamlit app using gTTS (no local file saving)
- `app_streamlit_pyttsx3.py` – Streamlit app using pyttsx3 (saves + deletes temp file)
- `app_gradio_gtts.py` – Gradio demo using gTTS and in-memory audio
- `utils/` – Optional utilities for voice config, audio handling, etc. (if you add them)

---

## Features

- Convert text into speech directly in your browser
- Option to use **online** or **offline** voice engines
- Clean UI for quick interaction
- Temporary audio cleanup handled automatically

---

## Requirements

- Python 3.7+
- Packages:
  - `gtts`
  - `pyttsx3`
  - `streamlit`
  - `gradio`

Install dependencies with:

```bash
pip install -r requirements.txt
