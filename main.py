import struct
import pyaudio
import pvporcupine
import sr
import json
from utils.log import *
import brain
from utils.speak import speak
from utils import eval_code
import os

porcupine = None
pa = None
audio_stream = None

_data = json.load(open("utils/data/data.json"))

debug_mode = _data["localVars"]["debug_mode"] # 1: On    0: Off
test_mode = _data["localVars"]["test_mode"] # 1: On    0: Off
try:
    porcupine = pvporcupine.create(
        access_key='access-key-here', 
        keyword_paths=["./assets/wake.ppn"]
    )
    
    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=porcupine.sample_rate, 
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length
                )
    print("nexus has booted.\n\n")
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            # wake word is detected
            if test_mode == 1:
                output = brain.think(eval_code.run())
                print(output)
                log('conversation', eval_code.run(), output)
                speak(output)
                continue
            query = sr.recognize().lower()

            # let Nexus think.
            output = brain.think(query)

            # if the output contains a prefix "COMMAND_" then it is a system command to be executed.
            if "COMMAND_" in output:
                command = output.replace("COMMAND_", "")
                if command == "REBOOT":
                    speak("Rebooting Nexus.")
                    log('adminLogs', 'SYSTEM REBOOT REQUESTED', 'system reboot granted.')
                    os.system("RUN.bat")
                    break
            else:
                speak(output)
            if debug_mode == 1:
                log('conversation', query, output)

except Exception as e:
    print(e)