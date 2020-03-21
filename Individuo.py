import random
import math

class Individuo(object):

    def __init__(self, tamanhoIndividuo):
        self.fitness = 0
        self.tamanhoIndividuo = tamanhoIndividuo
        self.materialGenetico = []
        for i in range(tamanhoIndividuo):
            self.materialGenetico.append(str(random.randint(0,1)))

    def calcularFitness(self):
        materialGeneticoStr = "".join(self.materialGenetico)
        materialGeneticoDecimal = int(materialGeneticoStr, 2)
        self.fitness = (3 * materialGeneticoDecimal) + math.pow(materialGeneticoDecimal, 2)
        return self.fitness

    