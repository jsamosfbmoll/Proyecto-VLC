from aleatoriedad_canciones import reconstruirLista, asignarRutas
import os


def verificarVLC():
    if os.access(r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "\"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe\""
    elif os.access(r"C:\Program Files\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "\"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe\""
    else:
        print("No tienes VLC")
        quit()
    return vlc


def reproducirCanciones():
    rutasCanciones = asignarRutas()
    rutaVLC = verificarVLC()
    comando = rutaVLC + " " + rutasCanciones + " --no-repeat"
    os.popen(comando)


if __name__ == "__main__":
    reproducirCanciones()