import random
import math
from Populacao import Populacao
import graficoFitnessMedio as grafico

TAMANHO_INDIVIDUO = 4
TAMANHO_POPULACAO = 2

populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO)
populacao.inicializar()


populacao.selecao()
populacao.reproducao()
populacao.mutacao()

grafico.plotar(populacao)