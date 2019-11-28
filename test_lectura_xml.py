from lectura_xml import *
import xml.etree.ElementTree as ET


def test_longitud_lista():
    nombres = getNombresCanciones()
    assert len(nombres) >= 6 #En el XML solo hay 6 canciones de las 50 que debe haber


def test_ruta_correcta(): #Se añadiran más posibilidades cuando el XML este lleno
    ruta = r"C:\Users\SEBAS\Desktop\Proyecto_VLC\musica\c-tangana-nino-de-elche-un-veneno-video-oficial.mp3"
    assert getRutaCancion("Welcome to the jungle") != ruta


def test_canciones_no_repetidas():
    canciones = getNombresCanciones()
    for cancion in canciones:
        assert False if canciones.count(cancion) > 1 else True


def test_comprobar_leerXML():
    raiz = leerXML()
    assert isinstance(raiz, ET.Element)


def test_ruta_valida():
    assert comprobarRuta("__pycache__") is True


def test_ruta_invalida():
    assert getRutaCancion("Never Again") is not None


def test_getInformacionCancion():
    infoCanciones = {"autor": "Guns 'N Roses",
                     "duracion": "3:59",
                     "genero": "Hard Rock"}
    assert getInformacionCancion("It's so easy") == infoCanciones


def test_getGenero():
    assert getGeneroCancion("1") == "Hard Rock"
