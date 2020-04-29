import random
import math


class Individuo(object):

    def __init__(self, tamanhoIndividuo):
        self.fitness = None        
        self.tamanhoIndividuo = tamanhoIndividuo
        self.materialGenetico = []
        for i in range(tamanhoIndividuo):
            self.materialGenetico.append(str(random.randint(0, 1)))
        self.calcularFitness()

    def reproducao(self, indiviuo2):
        filho = []
        for i in range(int(self.tamanhoIndividuo)): filho.append(-1)
        for i in range(int(self.tamanhoIndividuo)):
            if i <= int(self.tamanhoIndividuo/2):
                filho[i] = self.materialGenetico[i]
            else:
                filho[i] = indiviuo2.materialGenetico[i]
        return filho

    def calcularFitness(self):
        if(self.fitness == None):
            materialGeneticoStr = "".join(self.materialGenetico)
            materialGeneticoDecimal = int(materialGeneticoStr, 2)
            self.fitness = (3 * materialGeneticoDecimal) + \
                math.pow(materialGeneticoDecimal, 2)

        return self.fitness

    def fazerMutacao(self):
        print("Indivíduo: " + str(self.materialGenetico))

        # Sorteia um gene do indivíduo e inverte seu valor
        posicaoGene = random.randint(0, len(self.materialGenetico)-1)
        gene = self.materialGenetico[posicaoGene]
        print("Gene sorteado: " + str(gene))

        # Altera o gene (invertendo seu valor) e o coloca novamente no indiviuo
        novoGene = '0' if gene == '1' else '1'
        self.materialGenetico[posicaoGene] = novoGene
        print("Indivíduo mutado: " + str(self.materialGenetico))
