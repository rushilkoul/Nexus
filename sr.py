import speech_recognition as sr
from termcolor import colored
from utils import sound

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sound.play('wake')
        print(colored("listening...", "yellow"))
        r.pause_threshold = 1.7
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    
    try:
        sound.play("chime")
        print("processing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(colored(f" > {query}\n", 'cyan'))
    except Exception:
        return "error_could_not_recognize"
    
    
    return query