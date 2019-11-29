# Proyecto VLC

Desarrollado por José María Samos Y Sebastià Adrover

## Descripción del proyecto

Es un programa para Windows que genera una lista aleatoria de canciones a partir de un fichero xml que esta en el mismo directorio que el programa y luego las reproduce con VLC.

Usando la librería xml.etree.ElementTree para parsear el xml devuelve el nombre de las canciones y el módulo que se encarga de la capa lógica reordena la lista usando la librería random.

El módulo que representa la capa de servicios (la que invoca el VLC) contiene un método que muestra por orden las canciones en el que se van a reproducir, por cada canción muestra la información correspondiente.

El VLC se ejecuta automáticamente sin necesidad que el usuario deba interactuar con el programa a excepción de indicarle donde se encuentra el XML.

## Estructura del programa

El programa esta divido en tres capas y tres módulos correspondientes para cada capa más un módulo main que ejecuta el programa y contiene todas las llamadas a funciones.

1. lectura_xml.py
2. aleatoriedad_canciones.py
3. VLC_random_playlist.py
4. main.py

### lectura_xml.py (acceso a datos)

Este módulo se encarga de parsear el xml y sacar el nombre de las canciones, su ruta y la información adicional.

### aleatoriedad_canciones.py (lógica)

Este módulo se encarga de reordenar aleatoriamente la lista de canciones y de pedir la ruta de estas a lectura_xml.

### VLC_random_playlist.py

En este fichero python se busca la ruta al VLC, en caso de no encontralo debido a que no este instalado o no este en las carpetas de Program Files saltará un error, y muestra la información obtenida de las canciones por consola y ejecuta las canciones.

### main.py

Módulo con el que se inicia el programa, contiene todas las llamadas a las funciones de los demás módulos y permite que el código se ejecute correctamente.

## Módulos externos utilizados

1. xml.etree.ElementTree
2. os
3. random
4. tkinter
5. tkinter.filedialog