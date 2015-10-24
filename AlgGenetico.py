# -*- coding: utf-8 -*-
import random

class AlgGenetico:
	def __init__(self,data):
		self.data = data
		self.population =[]
		self.iteration = 1
		self.mutationF = 30 #mutation
		self.crossoverF = 80# crossover
		self.geneForGeneration =10 
		self.getInfo()
	#Generate first generation
	def firstGeneration (self, starting= None):
		#generate n solutions
		for i in range ( 0 , self.geneForGeneration):
			#generate configuration for each gene
			tmp = self.data.keys()
			solution = []
			first = True
			for j in range (0,len (self.data.keys())):
				if (first and (starting != None)):
					gene = starting
				else:
					gene = random.choice(tmp)
				tmp.remove(gene)
				solution.append (gene)
				first = False
			self.population.append(solution)


	def crossover (self):
		#any in population can cross
		for father in self.population:
			#cross or not cross
			if (random.choice (range(0,100)))<= self.crossoverF:
				#chose a pair (or itself)
				mother = random.choice(self.population)
				son = []
				for gene in range (0, len (father)):
					geneTemp = random.choice([father[gene], mother[gene]])
					while geneTemp in son:
						geneTemp = random.choice(self.data.keys())
					son.append(geneTemp)
#				if father == son or mother == son:
#					print "father = " + str (father)+" mother " + str (mother) +" son " + str (son) + " IGUAL" 
#				else:
#					print "father = " + str (father)+" mother " + str (mother) +" son " + str (son) 
				self.population.append(son)


	def naturalSelection(self):
		for i in self.population:
			while (self.population.count(i)> 1):
				self.population.remove (i)
		lista = self.population.sort(self.fitnessOrdenacao)
		novaLista = []
		for i in range (0, self.geneForGeneration):
			novaLista.append(self.population[i])
		self.population= novaLista
		return self.fitness(self.population[0])

	def mutation (self):
		#Any in population can receive mutation
		for i in self.population:
			#be or not be a mutation?
			if (random.choice(range(0,100)))<= self.mutationF:
				#chose aleatory gene
				alfa = 0
				beta = 0
				while (alfa == beta):
					alfa = random.randint (0, len (i)-1)
					beta = random.randint (0, len (i)-1)
				
				temp = i[alfa]
				i[alfa] = i[beta]
				i[beta] = temp 

	def fitness (self, solution):
		total = 0
		for i in range (0, len (solution)-1):
			total = total + self.data[solution[i]][solution [i+1]]
		#para fechar o circulo, somar distancia do ultimo ao primeiro
		total = total + self.data[solution[0]][solution[len (solution)-1]]
		return total

	def fitnessOrdenacao(self, solucaoA, solucaoB):
		if (self.fitness(solucaoA)>self.fitness(solucaoB)):
			return 1
		elif(self.fitness(solucaoA)< self.fitness(solucaoB)):
			return -1
		else:
			return 0
	def gravarArquivo (self, lista):
		arquivo = open ( "fitness.txt", "wr")
		for i in range (0, len (lista)):
			arquivo.write(str(i+1) + ":" + str(lista[i])+ "\n")
		arquivo.close()
			


	def getInfo ( self):
		geracoes = 10000
		self.firstGeneration()
		bestFit = 99999999999
		bestGen = 0
		fitness = []
		for i in range (0, geracoes):

			self.mutation()
			self.crossover()
			fit = self.naturalSelection()
			fitness.append(fit)
			if bestFit > fit:
				bestFit = fit
				bestGen = i
			print "Generation = "+ str ( i ) + " Fitness = " + str ( fit) 
		self.gravarArquivo(fitness)

