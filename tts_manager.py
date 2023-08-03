from gtts import gTTS
import os
from playsound import playsound

soundsPath = "sounds/"


def check_file_exists(path : str):
    return os.path.exists(path)

def create_dir(path: str):
    os.makedirs(path, exist_ok=True)

def readText(textToRead: str):
    #text_to_read.replace()
    filePath = f"{soundsPath}audio.mp3"

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