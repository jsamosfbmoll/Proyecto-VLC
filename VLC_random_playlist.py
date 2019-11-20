from aleatoriedad_canciones import reconstruirLista
import os
def verificarVLC():
    if os.access("C:\Program Files (x86)\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
    elif os.access("C:\Program Files\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "C:\Program Files\VideoLAN\VLC\vlc.exe"

def reproducirCancion():
    
    listaCanciones = reconstruirLista()
    rutaVLC = verificarVLC()

    
        
    
