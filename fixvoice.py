import librosa
import warnings
import soundfile
import streamlit as st
import torch
from io import BytesIO
from voicefixer import VoiceFixer


@st.cache_resource
def init_voicefixer():
    return VoiceFixer()


warnings.filterwarnings("ignore")
voice_fixer = init_voicefixer()
sample_rate = 44100
st.title("Fix Voice Audio")
st.divider()
uploaded_file = st.file_uploader("Upload a wav file", type="wav")
mode = st.radio("MODE: 0 - original | 1 - Add preprocessing | 2 - Add train", [0, 1, 2], index=0, horizontal=True)
if uploaded_file:
    if st.button("Run Inference"):
        with st.spinner("Inference..."):
            device = "cuda"
            voice_fixer._model = voice_fixer._model.to(device)
            audio, _ = librosa.load(uploaded_file, sr=sample_rate, mono=True)
            pred_wav = voice_fixer.restore_inmem(audio, mode=mode, cuda=True)
            st.divider()
            st.write("Original Audio : ")
            st.audio(uploaded_file)
            st.write("Inference output : ")
            with BytesIO() as buffer:
                soundfile.write(buffer, pred_wav.T, samplerate=sample_rate, format="WAV")
                st.audio(buffer.getvalue(), format="audio/wav")

