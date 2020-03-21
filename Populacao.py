from Individuo import Individuo
import random

class Populacao(object):

    def __init__(self, tamanhoPopulacao, tamanhoIndividuo):
        self.tamanhoPopulacao = tamanhoPopulacao
        self.tamanhoIndividuo = tamanhoIndividuo
        self.populacao = []

    def gerarPopulacao(self):
        for i in range(self.tamanhoPopulacao):
            individuo = Individuo(self.tamanhoIndividuo)
            self.populacao.append(individuo)
            print(individuo.materialGenetico)
    
    def calcularFitness(self):
        for i in range(self.tamanhoPopulacao):
            self.populacao[i].calcularFitness()
            print("Individuo {}: {}".format(i, self.populacao[i].fitness))
    
    def fazerMutacao(self):
        #Sorteia um indivíduo da população
        posicaoIndividuo = random.randint(0, len(self.populacao)-1)
        print("Posicao Indiviuo:" + str(posicaoIndividuo))
        self.populacao[posicaoIndividuo].fazerMutacao()

        