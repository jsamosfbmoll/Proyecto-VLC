from VLC_random_playlist import *
from aleatoriedad_canciones import *
from lectura_xml import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    root = Tk().withdraw()
    tipoDeFichero = (("Archivos XML", "*.xml"),)
    titulo = "Elige XML"
    rutaXML = askopenfilename(initialdir=".", title=titulo, filetypes=tipoDeFichero)

    raiz = leerXML(rutaXML)
    nombresCanciones = getNombresCanciones(raiz)
    cancionesReordenadas = reconstruirLista(nombresCanciones)
    rutasCanciones = asignarRutas(cancionesReordenadas, getRutaCancion, raiz)

    mostrarCanciones(cancionesReordenadas, getInformacionCancion, raiz)
    vlc = verificarVLC(lanzarError)

    reproducirCanciones(rutasCanciones, vlc)
    input()
