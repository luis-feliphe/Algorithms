# -*- coding: utf-8 -*-
from math import sqrt
class Leitor: 
	def __init__(self, endereco):
		arquivo = open (endereco, "r")
		self.lista = arquivo.readlines()
		self.mapaCidades = None
		self.solucoes=[]
		for i in range(0,len (self.lista)):
			self.lista[i] = self.lista[i].replace("\n", "")
		arquivo.close()

	def lerCoordenadas(self, file):
		pass
	def lerMatriz(self):
		print "Gerando mapa de mapas da matriz"
		mapaCidades= {}
		#calculando distancias entre cidades
		for i in range(0,len (self.lista)):
			nome, x, y = self.lista[i].split(" ")
			x, y = int (x), int (y)
			mapaDistancias = {}
			for j in range(0,len (self.lista)):
				nome2, xalvo, yalvo = self.lista[j].split(" ")
				xalvo, yalvo = int (xalvo), int (yalvo)
				distancia = sqrt((x-xalvo)**2) + ((y-yalvo)**2)
				mapaDistancias[nome2]= distancia
			mapaCidades[nome]= mapaDistancias
		self.mapaCidades = mapaCidades
		return self.mapaCidades

	def calculaValorSolucao (self, lista):
		total = 0
		for i in range(0, len(lista)-1):
			total = total + self.mapaCidades[lista[i]][lista[i+1]]
		return total




	def DSF(self, grafo, inicio = "1", visitados = None):
		if visitados == None:
			visitados= []
		visitados.append(inicio)
		if (len (visitados ) == len (grafo.keys())):
			visitados.append(visitados[0])
			print (visitados)
		proximos = set (grafo.keys()) - set (visitados)
		print ("meu id: " + str(inicio) + "  proximos : "+ str (proximos))
		for i in proximos:
			self.DSF(grafo, i, visitados)

	def func(self, noInicio, grafo, solucao=[], cont= 0):
		cont = cont +1 

		#solucao.append(noInicio)
		tmp = solucao 
		tmp.append(noInicio)
		print ( str  (cont) + " - "+str (solucao) + " O que resta " + str (len (set(grafo.keys()) - set (solucao))))
		#grafo.pop(noInicio)
		for i in set(grafo.keys()) - set (solucao) :
			print "\n Nova instancia gerada pelo ID " + str (noInicio)
			self.func(i, grafo, tmp, cont)


	def caminhosDFS(self, grafo, inicio, path=None):
		if path is None:
			path = [inicio]
		for next in (set(grafo[inicio].keys() ) - set(path)):
			yield self.caminhosDFS(grafo, next, path + [next])

	def algoritmoBuscaProfundidadeRecursivo(self, grafo, inicio, visitado=None, solucao = []):
		if visitado is None:
			visitado = set()
		visitado.add(inicio)
		solucao.append (inicio)
		if len ( set(grafo[inicio].keys()) -visitado )  == 0:
				print visitado
		for next in set(grafo[inicio].keys()) -visitado:
			self.algoritmoBuscaProfundidadeRecursivo(grafo, next, visitado, solucao)
		return visitado


	def algoritmoBuscaProfundidade(self, grafo , inicio):
		print (grafo.keys())
		solucao = []
		visitados, pilha = set(), [inicio]
		while pilha:
			vertice = pilha.pop()
			if vertice not in visitados:
				#solucao.append(vertice)
				visitados.add(vertice)
				pilha.extend(set(grafo[vertice].keys()) - visitados)
				#print "visitados= " + str (visitados) + "\n\n grafo: "+ str (pilha)  
				print "solucao " + str (solucao) +" valor " +  str (self.calculaValorSolucao(solucao))
				print "\n-------------------------------\n"

		return visitados
		

	def getGraph(self):
		pass

	def getLines(self):
		return self.lista
