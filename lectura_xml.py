import xml.etree.ElementTree as ET

def leerXML():
    arbol = ET.parse("libreria_canciones.xml")
    raiz = arbol.getroot()
    return raiz, arbol

def getNombresCanciones():
    raiz, arbol = leerXML()
    tracks = raiz[0][0][3]
    nombresCanciones = []

    if len(tracks) == 0:
        return []

    for track in tracks:
        nombreCancion = track.find("nombre").text
        nombresCanciones.append(nombreCancion)
    assert isinstance(nombresCanciones, list) and True if len(nombresCanciones) > 0 else False
    return nombresCanciones

def getRutaCancion(cancion):
    raiz, arbol = leerXML()
    albums = raiz.find("albums")

    for album in albums:
        tracks = album.find("tracks")
        for track in tracks:
            if track.find("nombre").text == cancion:
                rutaCancion = track.find("ruta").text
    return rutaCancion


if __name__ == "__main__":
    assert getNombresCanciones() == ["Welcome to the jungle"]
    assert getRutaCancion("Welcome to the jungle") == "desktop"