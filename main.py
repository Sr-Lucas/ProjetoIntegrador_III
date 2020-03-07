import random
import math

TAMANHO_INDIVIDUO = 10
TAMANHO_POPULACAO = 2

def gerarIndividuo(tamanhoIndividuo):
    individuo = []
    for i in range(tamanhoIndividuo):
       individuo.append(str(random.randint(0,1)))

    return individuo

def gerarPopulacao(tamanhoPopulacao):
    populacao = []
    for i in range(tamanhoPopulacao):
        populacao.append(gerarIndividuo(TAMANHO_INDIVIDUO))

    return populacao

def funcaoFitness(individuo):
    #Transforma o arrray de bits em string
    individuoStr = "".join(individuo)

    # Transforma a string de bits em um decimal
    individuoDec = int(individuoStr, 2)

    print("Ind: " + str(individuoDec))
    return (3 * individuoDec) + math.pow(individuoDec, 2)

pop = gerarPopulacao(5)

print("Fitness: " + str(funcaoFitness(gerarIndividuo(4))))
