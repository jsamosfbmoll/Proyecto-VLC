from lectura_xml import getNombresCanciones
import random

def reconstruirLista():    
    nombresCanciones = getNombresCanciones()
    assert isinstance(nombresCanciones, list)
    cancionesReordenadas = []
    for indice in range(0, len(nombresCanciones)):
        cancionesReordenadas.append(nombresCanciones[random.randrange(len(nombresCanciones))])
        nombresCanciones.remove(cancionesReordenadas[indice])
    assert len(nombresCanciones) == len(cancionesReordenadas)
    return cancionesReordenadas
