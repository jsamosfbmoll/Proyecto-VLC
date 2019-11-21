from lectura_xml import getNombresCanciones
import random

def reconstruirLista():    
    nombresCanciones = getNombresCanciones()
    copiaCanciones = nombresCanciones[:]
    assert isinstance(nombresCanciones, list)
    cancionesReordenadas = []
    for indice in range(0, len(nombresCanciones)):
        cancionesReordenadas.append(nombresCanciones[random.randrange(len(nombresCanciones))])
        nombresCanciones.remove(cancionesReordenadas[indice])
    assert len(copiaCanciones) == len(cancionesReordenadas)
    return cancionesReordenadas
