import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# import pyaudio
# import struct

# from pvorca import create, OrcaActivationLimitError
# orca = create(
#     access_key="here"
# )

# from pydub import AudioSegment
# from pydub.playback import play

# def play_pcm_audio(pcm_data, sample_width=2, channels=1):
#     # Create an AudioSegment from PCM data
#     audio = AudioSegment(pcm_data, sample_width=sample_width, channels=channels, frame_rate=orca.sample_rate)

#     # Play the audio
#     play(audio)



# def speak(text):
#     try:
#         pcm = orca.synthesize(text)
#         play_pcm_audio(struct.pack('%dh' % len(pcm), *pcm))
#     except OrcaActivationLimitError:
#         print('AccessKey has reached its processing limit')