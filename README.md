# Node2Vec

La ejecución cuenta con tres pasos:

1) Se ejecuta el archivo get_graph.py >output.edges. A éste se le da un archivo en formato palabra1\tpalabra2\tpeso
   Para cambiar el archivo de entrada se debe modificar el código. Asimismo el nombre de los archivos de salida.
   Este genera una lista de edges que se pasan a node2vec.
2) Se le da la lista de edges a node2vec. Ver README.
3) Node2Vec genera una lista con el formato de ids numéricos. Para obtener las palabras se ejecuta el archivo get_wordVector.py >output.vecs
   Este archivo toma de entrada la lista generada por node2vec y los archivos auxiliares obtenidos por get_graph.py. 
   Para modificar el archivo de entrada es necesario hacerlo desde el código.
