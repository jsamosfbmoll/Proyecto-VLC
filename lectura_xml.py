import xml.etree.ElementTree as ET
from os import access, F_OK
from tkinter import Tk, messagebox


def lanzarError(mensaje):
    root = Tk().withdraw()
    messagebox.showerror("Error", mensaje)
    return None


def leerXML(rutaXML):

    try:
        arbol = ET.parse(rutaXML)
    except ET.ParseError:
        lanzarError("El XML no esta bien formado")
        input()
        quit()

    raiz = arbol.getroot()
    return raiz


def getNombresCanciones(raiz):

    try:
        albums = raiz[0]
    except IndexError:
        print("El XML indicado no es correcto")
        input()
        quit()

    nombresCanciones = []

    for album in albums:
        try:
            tracks = album[3]
        except IndexError:
            print("El XML indicado no es correcto")
            input()
            quit()

        if len(tracks) == 0:
            return []

        for track in tracks:
            try:
                nombreCancion = track.find("nombre").text
                nombresCanciones.append(nombreCancion)
            except AttributeError:
                print("El XML indicado no es correcto")
                input()
                quit()

    assert isinstance(nombresCanciones, list)
    assert True if len(nombresCanciones) > 0 else False

    return nombresCanciones


def comprobarRuta(ruta):
    if access(ruta, F_OK):
        return True
    else:
        return False


def getRutaCancion(raiz, cancion):

    assert isinstance(cancion, str)
    assert cancion != ""

    try:
        albums = raiz.find("albums")
        albums.text
    except AttributeError:
        print("El XML indicado no es correcto")
        input()
        quit()

    rutaCancion = ""

    for album in albums:
        try:
            tracks = album.find("tracks")
            tracks.text
        except AttributeError:
            print("El XML indicado no es correcto")
            input()
            quit()
        for track in tracks:
            try:
                if track.find("nombre").text == cancion:
                    rutaCancion = track.find("ruta").text
            except AttributeError:
                print("El XML indicado no es correcto")
                input()
                quit()

    assert isinstance(rutaCancion, str)
    assert rutaCancion != ""

    if comprobarRuta(rutaCancion) is False:
        lanzarError("La ruta" + rutaCancion + ", no es una ruta válida.")
        return None

    return rutaCancion


def getGeneroCancion(raiz, idGenero):

    try:
        generos = raiz.find("generos")
        generos.text
    except AttributeError:
        print("El XML indicado no es correcto")
        input()
        quit()

    for genero in generos:
        try:
            if genero.attrib["id"] == idGenero:
                generoNombre = genero.find("nombre").text
        except AttributeError:
            print("El XML indicado no es correcto")
            input()
            quit()

    return generoNombre


def getInformacionCancion(raiz, cancion):

    try:
        albums = raiz.find("albums")
        albums.text
    except AttributeError:
        print("El XML indicado no es correcto")
        input()
        quit()
    informacionCancion = {}

    for album in albums:
        try:
            tracks = album.find("tracks")
            autor = album.find("autor").text
        except AttributeError:
            print("El XML indicado no es correcto")
            input()
            quit()
        for track in tracks:
            try:
                if track.find("nombre").text == cancion:
                    informacionCancion["autor"] = autor
                    informacionCancion["duracion"] = track.find("duracion").text
                    generoId = track.find("genero").attrib
                    genero = getGeneroCancion(raiz, generoId["id"])
                    informacionCancion["genero"] = genero
            except AttributeError:
                print("El XML indicado no es correcto")
                input()
                quit()
    return informacionCancion


if __name__ == "__main__":
    canciones = getNombresCanciones()
    for i in canciones:
        print(getInformacionCancion(i))
