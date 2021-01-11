# daicgrupo18

## Descripción del proyecto:
El objetivo de nuestro proyecto es implementar un dispositivo para ayudar a la población a hacer un uso debido de la mascarilla en el coche. Nuestro proyecto consiste en un dispositivo que esta conectado a una cámara la cual detecta si los usuarios del vehículo llevan mascarilla o no. Lo que hace el dispositivo es a la hora de iniciar el coche espera que se le pasen las tarjetas por el lector de NFC y una vez que sabe cuántos usuarios hay en el vehículo lo que hace es comienza a  escanear las caras de los diferentes integrantes del vehículo en el caso de que los usuarios lleven la mascarilla correctamente puesta el dispositivo emitirá un sonido para decir que todo esta correcto y se podrá producir al arranque del coche. En el caso de que no se este usando la mascarilla se emitirá un sonido durante 5 segundos y no dejaría arrancar el coche.

## Instalación y ejecución del dispositivo:
### Componentes necesarios:
- 1 Raspberry Pi.
- 2 Altavoz.
- 2 Botón.
- 1 Vibrador.
- 1 Lector NFC.
- 1 Python v3.7

### Descarga:
Para la descarga del programa hay que accede a nuestro repositorio de github en la siguiente url: https://github.com/JosebaVillanueva/daicgrupo18
> Se puede descargar directamente el zip o podemos clonar el repositorio can git clone.

### Puesta en marcha:
#### Una vez que tenemos los archivos del repositorio descargados podemos proceder a ejecutar el programa:
#### Ejecución en Windows
La parte de nuestro proyecto que se encarga de detectar la mascarilla la haremos en Windows ya que la raspberry no tiene suficiente poder de ejecución y por ello se queda atascada y no podríamos continuar con el resto del programa.
- Dentro del proyecto vamos a acceder a la carpeta de Detector de mascarilla.
- Una vez en la carpeta ejecutamos el siguiente comando el cmd de Windows: 
  - Ejecutamos pip install -r requirements.txt lo que hace esto es mirar dentro del txt y descarga el software necesario para que el programa de detección de las mascarillas funcione.
  - Una vez esta todo instalado podemos ejecutar el programa de detección de mascarillas directamente ya que toda la parte del algoritmo de detección ya está montado y listo para ejecutarse.  
  - El archivo train_mask_detector.py es el que se encarga de analizar todas fotos que están almacenadas en el dataset en la cual hay imágenes de ejemplo para que el programa aprenda a diferenciar entre mascarilla y no mascarilla.
  - Para ejecutar el programa lo que debemos hacer es ejecutar: python detect_mask_video.py el cual ejecutara el programa y mostrara alrededor de las caras de los usuarios un recuadro en verde y un texto diciendo que el usuario lleva mascarilla y un recuadro en rojo cuando el usuario no la lleva. Para terminar el proceso lo que hacemos es presionar la tecla ctrl + c y se acabara el proceso.
  - Una vez el proceso haya acabado se creara un archivo resultado.txt en el cual se almacena un resultado True o False dependiendo de si el uso de las mascarillas es com-o tiene que ser o no.   
- Una vez que tenemos el txt lo que hacemos es pasarlo a la raspberry para que el programa se ejecute dependiendo de el valor almacenado. Para ello utilizamos el siguiente comando: scp C:\Users\Joseba\Downloads\Detector-de-mascarilla\resultado.txt pi@daic18:/home/pi/Desktop/Proyecto

#### Ejecución en la Raspberry
Una vez tengamos los pasos anteriores realizado podremos ejecutar el programa.

Para ejecutarlo bastará con introducir el comando python proyecto.py. Como es obvio necesitaremos el documento que se ha creado en windows para que todo se ejecute correctamente. 
