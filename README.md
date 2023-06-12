# Fix Voice Audio
### A Python Streamlit app that restores bad voice audio using VoiceFixer
<hr>

Uses VoiceFixer model to load a bad audio file containing human voice.
<br>
it then tries to restore human speech regardless how much it is degraded. 
<br>
It can handle noise, reverb, low resolution and clipping.
<br>
All done within one model.

<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
git clone https://github.com/vluz/FixVoiceAudio.git
cd FixVoiceAudio
pip install -r requirements.txt
```

In some systems and configurations it might be necessary to install 
<br>
`linuxpackages.txt` and `linuxextrareqs.txt`
<br>
My aplogy for the ugly fix both with these and in the code.

On first run it may download several models.
<br>
The GUI may be blank or unresponsive for the duration of the setup
<br>
It will take quite some time, both on reqs above and on first run.
<br>
Please allow it time to finish.
<br>
All runs after the first are then faster to load.

To run do:<br>
`streamlit run fixvoice.py`

Gui will open on your default browser

<hr>

Note: Do not use this for production, it's untested
