import random


def reconstruirLista(nombresCanciones):

    copiaCanciones = nombresCanciones[:]

    assert isinstance(nombresCanciones, list)

    cancionesReordenadas = []
    for indice in range(0, len(nombresCanciones)):
        numeroAleatorio = random.randrange(len(nombresCanciones))
        cancionesReordenadas.append(nombresCanciones[numeroAleatorio])
        nombresCanciones.remove(cancionesReordenadas[indice])

    assert len(copiaCanciones) == len(cancionesReordenadas)

    return cancionesReordenadas


def asignarRutas(canciones, getRutaCancion, raiz):

    cancionesCopia = canciones[:]
    listaRutasCanciones = []

    for cancion in cancionesCopia:
        ruta = getRutaCancion(raiz, cancion)

        if ruta is None:
            canciones.remove(cancion)
        else:
            listaRutasCanciones.append("\"" + ruta + "\"")

    rutasCanciones = " ".join(listaRutasCanciones)
    return rutasCanciones
