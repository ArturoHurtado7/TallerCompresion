################################## README ##################################

Jaime Arturo Hurtado Romero   ja.hurtado905@uniandes.edu.co   cod. 201212121

############################################################################


Generalidades:

Se debe de extraer el archivo comprimido "TallerCompresion.zip", dentro de la carpeta encontrará una carpeta denominada source 
en donde encontrará dos archivos de python con extension ".py", uno para cada algoritmo, otro para la interfaz y utilidades.

* main.py           --> (Interface) contiene el fujo 
* huffman.py        --> (Algoritmo) contiene las funciones para realizar el algoritmo.
* shannon_fano.py   --> (Algoritmo) contiene las funciones para realizar el algoritmo.
* utils.py          --> (Utilidades) funciones generales.


Para ejecutar el algoritmo deberá ejecutar el archivo main.py desde la terminal y estar ubicado dentro del folder de source.
La ejecución del progama main.py debe contener el nombre del archivo de entrada y salida, como se muestra en el siguiente ejemplo:

> cd "D:\Maestria\Proyecto\source"                                          <- comando para ubicarse en la carpeta source
> python main.py -i ./input.txt -o ./output.txt -a compress -c huffman      <- comando para ejecutar el programa main.py

> py main.py -i ../tests/input.txt -o ./output.txt -a compress -c shannon_fano

existen 4 parametros los cuales son requeridos:

--input ó i     : parametro que indica la ruta del archivo de entrada.
--output ó o    : parametro que indica la ruta del archivo de salida.




############################################################################