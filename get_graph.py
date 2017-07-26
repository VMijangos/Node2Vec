from csv import reader
import networkx as nx
import matplotlib.pyplot as plt
from pickle import dump

# Abre el archivo, cada par de pares es una linea y cada palabra en el par esta separado por tabulador
pairs = list( reader(open('esna.lemma_morph.anym.nostop','r'),delimiter='\t') )

#Genera las listas de pares para cada lengua
na_ids = []
es_ids = []
edges = []
for p in pairs:
	w = float(p[2])  #El lugar que ocupa el peso en el archivo de entrada
	if w > 0:
		edges.append( (p[0].strip(), p[1].strip(), w) )
		na_ids.append(p[0].strip())
		es_ids.append(p[1].strip())

#Genera el grafo
G = nx.Graph()
G.add_weighted_edges_from(edges)

#Genera lista de ids y el vocabulario
ids = {i:w for i,w in enumerate(G.nodes())}
voc = {k:j for j,k in ids.iteritems()}

#Imprime el grafo en formato para node2vec con >output.edges
count = 0
for u,v,w in G.edges(data='weight'):
	print voc[u], voc[v],w
	count += 1

#Genera los datos necesarios para construir el grafo
f = open('dataAll.esna.lemma_morph.anym.nostop.p','w')
dump([G,ids,voc,na_ids,es_ids],f)
f.close()
