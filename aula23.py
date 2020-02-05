import numpy as np
import pandas as pd
import random
import math

from scipy import stats


random.seed(100)

# Primeiros Passos

# Dados do Exercício

# Tempo das Tarefas

mediaTempo =  # Preencher com os dados do exercício
qtdeTempo =  # Preencher com os dados do exercício
desvioTempo =  # Preencher com os dados do exercício
melhoraTempo = 0.15

# Qualidade das Tarefas

mediaQuali =  # Preencher com os dados do exercício
qtdeQuali =  # Preencher com os dados do exercício
desvioQuali =  # Preencher com os dados do exercício
melhoraQuali = 0.05

# Tempo das Tarefas

mediaAval =  # Preencher com os dados do exercício
qtdeAval =  # Preencher com os dados do exercício
melhoraAval = 0.24

# Tempo das Tarefas

mediaSatis =  # Preencher com os dados do exercício
qtdeSatis =  # Preencher com os dados do exercício
desvioSatis =  # Preencher com os dados do exercício
melhoraSatis = 0.2

# O primeiro passo da análise é gerar uma pseudo amostra com os valores iniciais das variáveis.
# Para fazermos isto, utilizamos os valores de referência da distribuição final
# e defasamos de acordo com o aumento observado, previamente registrado.

dataTempo = np.random.lognormal(mean=math.log(mediaTempo), sigma=math.log(desvioTempo), size=qtdeTempo)
dataQuali = np.random.lognormal(mean=math.log(mediaQuali), sigma=math.log(desvioQuali), size=qtdeQuali)
dataAval = np.random.exponential(scale=mediaAval, size=qtdeAval)
dataSatis = np.random.lognormal(mean=math.log(mediaSatis), sigma=math.log(desvioSatis), size=qtdeSatis)

antesTempo = np.random.lognormal(mean=math.log(mediaTempo/melhoraTempo), sigma=math.log(desvioTempo), size=qtdeTempo)
antesQuali = np.random.lognormal(mean=math.log(mediaQuali/melhoraQuali), sigma=math.log(desvioQuali), size=qtdeQuali)
antesAval = np.random.exponential(scale=mediaAval/melhoraAval, size=qtdeAval)
antesSatis = np.random.lognormal(mean=math.log(mediaSatis/melhoraSatis), sigma=math.log(desvioSatis), size=qtdeSatis)

# Gerada a amostra, precisamos transformar os dados em uma distribuição normal a fim de realizar
# os testes de hipótese. No caso das lognormais, basta fazer o teste com o log dos valores.
# Já no caso da exponencial, é necessário fazer a normalização

desvioAval = np.std(dataAval)
normalAval = (dataAval-mediaAval)/desvioAval

desvantAval = np.std(antesAval)
normantAval = (antesAval-(mediaAval/melhoraAval))/desvantAval

# Agora, é só correr os testes T nas amostras

stats.ttest_ind(dataTempo, antesTempo)
stats.ttest_ind(dataQuali, antesQuali)
stats.ttest_ind(normalAval, normantAval)
stats.ttest_ind(dataSatis, antesSatis)