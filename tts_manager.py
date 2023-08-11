from gtts import gTTS
import os
from playsound import playsound

soundsPath = "sounds/"
filePath = f"{soundsPath}audio.mp3"


def check_file_exists(path : str) -> bool:
    return os.path.exists(path)

def create_dir(path: str):
    os.makedirs(path, exist_ok=True)

def readText(textToRead: str):
    if(len(textToRead) <= 0):
        #textToRead = "No hay texto para leer"
        return
    #text_to_read.replace()
    #filePath = f"{soundsPath}audio.mp3"
    
    if not check_file_exists(soundsPath):
        create_dir(soundsPath)

    if check_file_exists(filePath):
        os.remove(filePath)
    
    create_new_audio(textToRead, filePath)
    playsound(filePath)
    return

def create_new_audio(textToRead: str, filePath: str):
    
    ttsData = gTTS(text=textToRead, lang="es")
    ttsData.save(filePath)