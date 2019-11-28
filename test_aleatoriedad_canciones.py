from aleatoriedad_canciones import reconstruirLista, asignarRutas


def test_aleatoria_cantidad():
    assert len(reconstruirLista()) >= 8


def test_aleatoria_no_repetidos():
    canciones = reconstruirLista()
    for cancion in canciones:
        if canciones.count(cancion) > 1:
            assert False
    assert True


def test_asignar_rutas_primer_valor():
    assert isinstance(asignarRutas()[0], str)


def test_asignar_rutas_segundo_valor():
    assert isinstance(asignarRutas()[1], list)