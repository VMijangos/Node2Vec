from __future__ import division
from pickle import load
from utils import plot_vecs
import numpy as np
from operator import itemgetter
 
#Abre los archivos auxiliares
G,ids,voc,na_ids,es_ids = load(open('dataAll.esna.lemma_morph.anym.nostop.p','r'))
ref = {h:k for h,k in voc.iteritems()}
 
#abre los embeddings obtenidos por node2vec
f = open('esna-lemma_morph-anim-nonstop.emd','r').read().strip().split('\n')
f.pop(0)
 
#Imprime los datos de n2v en el formato palabra vector
V = np.zeros((len(ids),128))
for v in f:
    todo = v.split()
    id = int(todo[0])
    todo.pop(0)
    V[id] =  np.array([float(x) for x in todo])
    print ids[id], np.array([float(x) for x in todo])
