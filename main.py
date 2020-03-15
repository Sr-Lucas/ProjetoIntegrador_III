import random
import math

TAMANHO_INDIVIDUO = 4
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

def mutacao(populacao):
    print(populacao)

    #Sorteia um indivíduo da população
    posicaoIndividuo = random.randint(0, len(populacao)-1)
    print("Posicao Indiviuo:" + str(posicaoIndividuo))
    individuo = populacao[posicaoIndividuo]
    print("Indivíduo: " + str(individuo))

    #Sorteia um gene do indivíduo e inverte seu valor
    posicaoGene = random.randint(0, len(individuo)-1)
    gene = individuo[posicaoGene]
    print("Gene sorteado: " + str(gene))

    #Altera o gene (invertendo seu valor) e o coloca novamente no indiviuo
    novoGene = '0' if gene == '1' else '1'
    individuo[posicaoGene] = novoGene
    print("Novo Indivíduo: " + str(individuo))

    populacao[posicaoIndividuo] = individuo

pop = gerarPopulacao(5)
mutacao(pop)