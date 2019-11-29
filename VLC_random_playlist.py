import os


def verificarVLC(lanzarError):

    if os.access(r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "\"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe\""
    elif os.access(r"C:\Program Files\VideoLAN\VLC\vlc.exe", os.F_OK):
        vlc = "\"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe\""
    else:
        lanzarError("No tienes VLC")
        quit()

    return vlc


def mostrarCanciones(canciones, getInformacionCancion, raiz):

    print("Las canciones se reproducirán en este orden: ")

    for cancion in canciones:
        informacionCancion = getInformacionCancion(raiz, cancion)
        print("  " + cancion)
        print("     Autor: " + informacionCancion["autor"])
        print("     Duración: " + informacionCancion["duracion"])
        print("     Genero: " + informacionCancion["genero"])
        print()

    return None


def reproducirCanciones(rutasCanciones, rutaVLC):

    comando = rutaVLC + " " + rutasCanciones + " --no-repeat"

    os.popen(comando)
    return None
