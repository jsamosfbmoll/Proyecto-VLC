import xml.etree.ElementTree as ET
from os import access, F_OK
from tkinter import Tk, messagebox


def lanzarError(mensaje):
    root = Tk().withdraw()
    messagebox.showerror("Error", mensaje)
    return None


def leerXML():

    try:
        arbol = ET.parse("libreria_canciones.xml")
    except ET.ParseError:
        lanzarError("El XML no esta bien formado")
        quit()

    raiz = arbol.getroot()
    return raiz


def getNombresCanciones():

    raiz = leerXML()
    albums = raiz[0]
    nombresCanciones = []

    for album in albums:
        tracks = album[3]

        if len(tracks) == 0:
            return []

        for track in tracks:
            nombreCancion = track.find("nombre").text
            nombresCanciones.append(nombreCancion)

    assert isinstance(nombresCanciones, list)
    assert True if len(nombresCanciones) > 0 else False

    return nombresCanciones


def comprobarRuta(ruta):
    if access(ruta, F_OK):
        return True
    else:
        return False


def getRutaCancion(cancion):

    assert isinstance(cancion, str)
    assert cancion != ""

    raiz = leerXML()
    albums = raiz.find("albums")
    rutaCancion = ""

    for album in albums:
        tracks = album.find("tracks")
        for track in tracks:
            if track.find("nombre").text == cancion:
                rutaCancion = track.find("ruta").text

    assert isinstance(rutaCancion, str)
    assert rutaCancion != ""

    if comprobarRuta(rutaCancion) == False:
        lanzarError("La ruta" + rutaCancion + ", no es una ruta válida.")
        return None

    return rutaCancion


def getGeneroCancion(idGenero):

    raiz = leerXML()
    generos = raiz.find("generos")
    for genero in generos:
        if genero.attrib["id"] == "1":
            generoNombre = genero.find("nombre").text

    return generoNombre


def getInformacionCancion(cancion):
    raiz = leerXML()

    albums = raiz.find("albums")
    informacionCancion = {}

    for album in albums:
        tracks = album.find("tracks")
        autor = album.find("autor").text
        for track in tracks:
            if track.find("nombre").text == cancion:
                informacionCancion["autor"] = autor
                informacionCancion["duracion"] = track.find("duracion").text
                generoId = track.find("genero").attrib
                informacionCancion["genero"] = getGeneroCancion(generoId["id"])
    return informacionCancion


if __name__ == "__main__":
    assert len(getNombresCanciones()) == 6
    assert getRutaCancion("Welcome to the jungle") == r"C:\Users\Dual\Desktop"
