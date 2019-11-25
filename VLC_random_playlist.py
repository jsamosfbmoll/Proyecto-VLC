from aleatoriedad_canciones import reconstruirLista
import os
def verificarVLC():
    if os.access(r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "\"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe\""
    elif os.access(r"C:\Program Files\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    else:
        print("No tienes VLC")
    return vlc

def reproducirCancion():
    
    listaCanciones = reconstruirLista()
    rutaVLC = verificarVLC()
    cancion = "\"C:\\Users\\SEBAS\\Desktop\\fp dual\\Sistemes Informatics\\carpeta_VLC\""
    variable = rutaVLC + " " + cancion
    print(variable)
    os.popen(variable)
    
        
if __name__ == "__main__":
    #assert verificarVLC() == r"'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe'"

    reproducirCancion()