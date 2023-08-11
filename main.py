#import getpass
import time
import keyboard
from clipboard_manager import ClipboardGetter
from tts_manager import readText

program_running = True
readHotkey = "f3"
stopProgramKey = "f10"


readText("Bienvenido")
print("Utilice f3 para que el programa lea el texto que tengas copiado \n"
      + "para copiar texto podes usar el atajo Ctrl + C o Click derecho, Copiar \n " +
      "para salir del programa presione f10")


keyboard.add_hotkey(readHotkey, lambda: read_hotkey_action(), suppress=True)


def read_hotkey_action():
    # here you need to check if the program is already reading and stop that
    keyboard.press("ctrl")
    keyboard.press_and_release("c")
    keyboard.release("ctrl")
    time.sleep(0.1)
    
    readText(ClipboardGetter.get_clipboard_text())

def stop_reading():
    pass
    #thread = None


keyboard.wait(stopProgramKey)
readText("Cerrando Programa")


