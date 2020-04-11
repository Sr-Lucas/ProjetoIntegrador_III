from Individuo import Individuo
import random
import sys

class Populacao(object):

    def __init__(self, tamanhoPopulacao, tamanhoIndividuo):
        self.populacao = []
        self.contadorGeracao = 1
        self.geracoes = [1]
        self.fitnessMedioDasGeracoes = []
        self.individuoMaiorFitness = []
        self.segIndividuoMaiorFitness = []
        self.tamanhoPopulacao = tamanhoPopulacao
        self.tamanhoIndividuo = tamanhoIndividuo

    def inicializar(self):
        for i in range(self.tamanhoPopulacao):
            individuo = Individuo(self.tamanhoIndividuo)
            self.populacao.append(individuo)
            print(individuo.materialGenetico)
        self.fitnessMedioDasGeracoes.append(self.calcularFitnessMedio())
    
    def calcularFitnessMedio(self):
        fitnessTotal = 0
        for i in range(self.tamanhoPopulacao):
            fitnessTotal += self.populacao[i].calcularFitness()
        
        return fitnessTotal / self.tamanhoPopulacao
    
    def mutacao(self):
        #Sorteia um indivíduo da população
        posicaoIndividuo = random.randint(0, len(self.populacao)-1)
        print("Posicao Indiviuo:" + str(posicaoIndividuo))
        self.populacao[posicaoIndividuo].fazerMutacao()

    def selecao(self):
        melhorFitness = self.populacao[0]
        segundoMelhorFitness = self.populacao[0]
        for individuo in self.populacao:
            fitness = individuo.calcularFitness()
            if (fitness > melhorFitness.calcularFitness()):
                segundoMelhorFitness = melhorFitness
                melhorFitness = individuo

            elif (fitness > segundoMelhorFitness.calcularFitness()):
                segundoMelhorFitness = individuo
    
    def reproducao(self):
        indvHalf = len(self.individuoMaiorFitness)/2
        filho = []

        for i in range(len(self.individuoMaiorFitness)):
            if i < indvHalf:
                filho.append(self.individuoMaiorFitness[i])
            else:
                filho.append(self.segIndividuoMaiorFitness[i])

        return filho

    def adicionarDescendente(self, descendente):
        menorFitness = sys.float_info.max

        for indice,individuo in enumerate(self.populacao):
            if (individuo.calcularFitness() < menorFitness):
                indiceMenorFitness = indice
    
        self.populacao[indiceMenorFitness] = descendente

        #Incrementa o contador de geracoes
        self.contadorGeracao += 1
        #Coloca mais uma geracao no array de geracoes e seu respectivo fitness médio no array 'fitness'
        self.geracoes.append(self.contadorGeracao)
        self.fitnessMedioDasGeracoes.append(self.calcularFitnessMedio())

        