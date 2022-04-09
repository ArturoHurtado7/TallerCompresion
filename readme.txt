################################## README ##################################

Jaime Arturo Hurtado Romero   ja.hurtado905@uniandes.edu.co   cod. 201212121
Hernan David Cuy Salcedo      h.cuy@uniandes.edu.co           cod. 202019100

############################################################################

Generalidades:

Se debe de extraer el archivo comprimido "TallerCompresion.zip", dentro de la carpeta encontrará una carpeta denominada source 
en donde encontrará dos archivos de python con extension ".py", uno para cada algoritmo, otro para la interfaz y utilidades.

* main.py           --> (Interface) contiene el fujo 
* huffman.py        --> (Algoritmo) contiene las funciones necesarias para ejecutar el algoritmo.
* shannon_fano.py   --> (Algoritmo) contiene las funciones necesarias para ejecutar el algoritmo.
* utils.py          --> (Utilidades) funciones generales.

Para ejecutar el algoritmo deberá ejecutar el archivo main.py desde la terminal al estar ubicado dentro de la carpeta "/source".
La ejecución del programa main.py debe contener el nombre del archivo de entrada, como se muestra en los siguientes ejemplos:

> cd "D:\Maestria\Proyecto\source"                  <- comando para ubicarse en la carpeta source

> python main.py -i "./input.txt" -c huffman        <- comando para ejecutar el programa main.py con compresion huffman
> python main.py -i "./input.txt" -c shannon_fano   <- comando para ejecutar el programa main.py con compresion shannon_fano

existen 2 parámetros los cuales son requeridos:

--input ó -i        <- parámetro que indica la ruta del archivo de entrada.
--compression ó -c  <- parámetro que indica tipo de compresión.

se generarán 2 archivos de salida en la misma carpeta de entrada:

input_comp.bin      <- archivo binario con el contenido comprimido
input_stats.txt     <- archivo de texto con las métricas y las llaves

adicionalmente se muestra en pantalla los textos: originales, comprimidos y descomprimidos
junto con los diccionarios para realizar las operaciones de compresión y descompresión.

############################################################################