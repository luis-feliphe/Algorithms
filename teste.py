# -*- coding: utf-8 -*-

from Leitor import Leitor
from AlgGenetico import  AlgGenetico
l = Leitor ("teste.txt")
x = l.lerMatriz()
#print (l.algoritmoBuscaProfundidadeRecursivo(x, "1"))
#l.DSF(x, "1")
#l.func("1", x)
alg = AlgGenetico (x)
 
