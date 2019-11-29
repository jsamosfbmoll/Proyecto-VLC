from aleatoriedad_canciones import reconstruirLista, asignarRutas
from lectura_xml import getNombresCanciones, leerXML, getRutaCancion


def test_aleatoria_cantidad():
    assert len(reconstruirLista(getNombresCanciones(leerXML("libreria_canciones.xml")))) >= 8


def test_aleatoria_no_repetidos():
    canciones = reconstruirLista(getNombresCanciones(leerXML("libreria_canciones.xml")))
    for cancion in canciones:
        if canciones.count(cancion) > 1:
            assert False
    assert True


def test_asignar_rutas_primer_valor():
    canciones = reconstruirLista(getNombresCanciones(leerXML("libreria_canciones.xml")))
    assert isinstance(asignarRutas(canciones, getRutaCancion, leerXML("libreria_canciones.xml")), str)