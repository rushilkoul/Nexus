from playsound import playsound

def play(sound):
    if sound == 'wake':
        playsound("./assets/wake.mp3", block=False)
    elif sound == 'chime':
        playsound("./assets/chime.mp3", block=False)