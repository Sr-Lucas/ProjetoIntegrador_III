import matplotlib.pyplot

def plotar(populacao):
    matplotlib.pyplot.title('Gráfico do Fitness das gerações')
    matplotlib.pyplot.xlabel('Geração')
    matplotlib.pyplot.ylabel('Fitness médio')
    matplotlib.pyplot.plot(populacao.geracoes, populacao.fitnessMedioDasGeracoes)
    matplotlib.pyplot.show()