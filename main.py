import getpass
import keyboard
from clipboard_manager import ClipboardGetter
from tts_manager import readText

program_running = True
hotkey = "f3"
stopProgramKey = "f10"

#readText("Bienvenido, " + getpass.getuser())

print("Utilice f3 para que el programa lea el texto que tengas copiado \n"
      + "para copiar texto podes usar el atajo Ctrl + C o Click derecho, Copiar \n " +
      "para salir del programa presione f10")

#TTSManager.dispose_sounds()
keyboard.add_hotkey(hotkey, lambda: hotkeyAction())

def hotkeyAction():
    readText(ClipboardGetter.get_clipboard_text())


keyboard.wait(stopProgramKey)
readText("Cerrando Programa")
    


