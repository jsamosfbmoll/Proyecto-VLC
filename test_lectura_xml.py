from lectura_xml import *
import xml.etree.ElementTree as ET


def test_longitud_lista():
    nombres = getNombresCanciones()
    assert len(nombres) >= 6 #En el XML solo hay 6 canciones de las 50 que debe haber


def test_ruta_correcta(): #Se añadiran más posibilidades cuando el XML este lleno
    assert getRutaCancion("Welcome to the jungle") == r"C:\Users\SEBAS\Desktop\Proyecto_VLC\musica\c-tangana-nino-de-elche-un-veneno-video-oficial.mp3"


def test_canciones_no_repetidas():
    canciones = getNombresCanciones()
    for cancion in canciones:
        assert False if canciones.count(cancion) > 1 else True


def test_comprobar_leerXML():
    raiz, arbol = leerXML()
    assert isinstance(raiz, ET.Element)
    assert isinstance(arbol, ET.ElementTree)


def test_ruta_valida():
    assert comprobarRuta("__pycache__") == True


def test_ruta_invalida():
    assert getRutaCancion("Never Again") == None