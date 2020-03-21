from Individuo import Individuo

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