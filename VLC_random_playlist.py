import xml.etree.ElementTree as ET

def leerXML():
    arbol = ET.parse("libreria_canciones.xml")
    raiz = arbol.getroot()
    return raiz, arbol

def getNombresCanciones():
    raiz, arbol = leerXML()
    tracks = raiz[0][0][3]
    nombresCanciones = []
    for track in tracks:
        nombreCancion = track.find("nombre").text
        nombresCanciones.append(nombreCancion)
    return nombresCanciones

if __name__ == "__main__":
    assert getNombresCanciones() == ["Welcome to the jungle"]