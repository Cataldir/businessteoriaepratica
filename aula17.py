import numpy as np
import pandas as pd
import random

# Criando o vetor de dados.
# Em um caso empírico real, estes dados serão transmitidos por alguma política de captação.
# Ainda que estas políticas estejam fora do escopo do curso, você pode pesquisar web crawlers e
# entender como pode capturar informações externas aos dados da empresa

random.seed(100)


# Trabalhistas

trbProb = np.random.binomial(n=500, p=0.35, size=500)

def trbImp(n):
	return 500*n

Trb = trbImp(trbProb)

# Baixa Aderência

adrProb = np.random.binomial(n=500, p=0.6, size=500)

def adrImp(n):
	return 1200*n

Adr = adrImp(adrProb)

# Custos

cstProb = np.random.binomial(n=500, p=0.4, size=500)

def cstImp(n):
	return 800*n

Cst = cstImp(cstProb)

# Impossibilidade de Remunerar

remProb = np.random.binomial(n=500, p=0.2, size=500)

def remImp(n):
	return 8000*n

Rem = remImp(remProb)

# Diminuição da Cooperatividade

cooProb = np.random.binomial(n=500, p=0.1, size=500)

def cooImp(n):
	return 20000*n

Coo = cooImp(cooProb)

### Momentos

# Trabalho

momTrb = [np.mean(trbProb), np.var(trbProb)**0.5]
momResTrb = [np.mean(Trb), np.var(Trb)**0.5]

momAdr = [np.mean(adrProb), np.var(adrProb)**0.5]
momResAdr = [np.mean(Adr), np.var(Adr)**0.5]

momCst = [np.mean(cstProb), np.var(cstProb)**0.5]
momResCst = [np.mean(Cst), np.var(Cst)**0.5]

momRem = [np.mean(remProb), np.var(remProb)**0.5]
momResRem = [np.mean(Rem), np.var(Rem)**0.5]

momCoo = [np.mean(cooProb), np.var(cooProb)**0.5]
momResCoo = [np.mean(Coo), np.var(Coo)**0.5]


### Tratamento

# O tratamento dos dados, de forma prática, exige três procedimentos:
# Remoção de extremos (outliers), seguindo um critério de identificação (nesse caso, quando for 
# maior que três desvios padrão da amostra).
# Normalização ou Padronização, que é quando calculamos a diferença da observação para a média e
# dividimos pelo desvio padrão. Nesse caso, os dados passam a seguir uma distribuição normal.
# Por fim, retiramos todos os valores inválidos (NA) da amostra tratada (podemos fazer isso como 
# primeiro passo também.)

# Elementos de Teste

crtTrb = [momTrb[0]-3*momTrb[1], momTrb[0]+3*momTrb[1]]
crtAdr = [momAdr[0]-3*momAdr[1], momAdr[0]+3*momAdr[1]]
crtCst = [momCst[0]-3*momCst[1], momCst[0]+3*momCst[1]]
crtRem = [momRem[0]-3*momRem[1], momRem[0]+3*momRem[1]]
crtCoo = [momCoo[0]-3*momCoo[1], momCoo[0]+3*momCoo[1]]

# Remoção de Outliers

TrbTreat = trbProb[(trbProb > crtTrb[0]) & (trbProb < crtTrb[1])]
AdrTreat = adrProb[(adrProb > crtAdr[0]) & (adrProb < crtAdr[1])]
CstTreat = cstProb[(cstProb > crtCst[0]) & (cstProb < crtCst[1])]
RemTreat = remProb[(remProb > crtRem[0]) & (remProb < crtRem[1])]
CooTreat = cooProb[(cooProb > crtCoo[0]) & (cooProb < crtCoo[1])]

# Checamos o tamanho de cada vetor:

len(TrbTreat)
len(AdrTreat)
len(CstTreat)
len(RemTreat)
len(CooTreat)

# Normalização

TrbTreat = (trbProb-momTrb[0])/momTrb[1]
AdrTreat = (adrProb-momAdr[0])/momAdr[1]
CstTreat = (cstProb-momCst[0])/momCst[1]
RemTreat = (remProb-momRem[0])/momRem[1]
CooTreat = (cooProb-momCoo[0])/momCoo[1]

# Estruturando o Data Frame padronizado - linhas mostram os dados válidos do experimento.

dfProb = pd.DataFrame({'trabalho': TrbTreat, 'aderencia': AdrTreat, 'custo': CstTreat, 'rem': RemTreat, 'coop': CooTreat})