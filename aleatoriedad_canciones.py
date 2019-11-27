from lectura_xml import getNombresCanciones, getRutaCancion
import random


def reconstruirLista():    
    nombresCanciones = getNombresCanciones()
    copiaCanciones = nombresCanciones[:]
    assert isinstance(nombresCanciones, list)
    cancionesReordenadas = []
    for indice in range(0, len(nombresCanciones)):
        numeroAleatorio = random.randrange(len(nombresCanciones))
        cancionesReordenadas.append(nombresCanciones[numeroAleatorio])
        nombresCanciones.remove(cancionesReordenadas[indice])
    assert len(copiaCanciones) == len(cancionesReordenadas)
    return cancionesReordenadas


def asignarRutas():
    canciones = reconstruirLista()
    listaRutasCanciones = []
    for cancion in canciones:
        listaRutasCanciones.append("\"" + getRutaCancion(cancion) + "\"")
    rutasCanciones = " ".join(listaRutasCanciones)
    return rutasCanciones, canciones
