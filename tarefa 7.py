import numpy as np
import pandas as pd
import unidecode as ud

import rpy2.robjects as ro

from rpy2.robjects.packages import importr
from scipy.stats import ttest_ind as htest
from scipy.stats import ttest_1samp as atest

# Usaremos alguns pacotes do R nesta aula:

base = importr('base') # pacote base do R
stats = importr('stats') # pacote stats do R
fitdist = importr('fitdistrplus') # pacote fitdistrplus do R

"""
	É possível criar sessões do R dentro de um programa de Python com o rpy2. Assim, 
	vamos fazer o uso da biblioteca fitdistrplus, que é utilizada para avaliar quão bem
	um conjunto de dados se encaixa em uma distribuição de probabilidade, para podermos
	avaliar qual a distribuição associada aos dados de processos que temos.

	Para instalar o pacote, é necessário que se faça por uma sessão do R.
	Abra o terminal e inicie uma sessão do R
	> R
	
	após iniciar a sessão, instale o pacote fitdistrplus
	> install.packages('fitdistrplus')

	após finalizar a instalação, saia da sessão de R
	> q()

	e inicie a sessão de python
	> python3.8 (ou python3, caso você só tenha uma sessão de python instalada)
"""

# Não precisamos arrumar o DF neste caso
inputs = pd.read_excel("Análise de Prospecto.xlsx", sheet_name="Resources", delimiter=",")
process = pd.read_excel("Análise de Prospecto.xlsx", sheet_name="Process", delimiter=",")

def generate_data(df, shape_param=5, dist=stats.rweibull):
	data = pd.DataFrame()
	for i in range(len(df)):
		name = ud.unidecode(df.iloc[i]['Name'])
		mean = float(df.iloc[i]['Avg. time (m)']) # colocamos o objeto como um float para exportação
		inst = np.max(df['Instances completed']) # colocamos o objeto como um int para exportação
		param = mean/(base.gamma(1+1/shape_param)[0]) # geramos o parâmetro de escala a ser utilizado na Weibull
		estm_data = np.array(dist(int(inst), shape = shape_param, scale = param))
		data[name] = estm_data
	return data

prc_data = generate_data(process)

def check_outlier(df, level):
	names = df.columns
	outlier = pd.DataFrame()
	for name in names:
		outlier[ud.unidecode(name)] = (df[name] > np.mean(df[name])+level*np.std(df[name]))
	return outlier

outliers = check_outlier(prc_data, 3)

# para checar quantos eventos de erros possui uma tarefa simulada, basta trocar o índice da série
outliers[outliers.columns[0]].value_counts()
# para checar quantos erros haviam sido encontrados na tarefa, calcule o seguinte:
np.max(process['Instances completed']) - process['Instances completed'][0]
# trocando o último índice pelo equivalente à tarefa.

"""
	Por exemplo, se você quiser chegar se o processo simulado teve mais ou menos erros do que o
	processo original, você escreve:
	
	outliers[outliers.columns[0]].value_counts()[True] < np.max(process['Instances completed']) - process['Instances completed'][0]
	
	Se for verdadeiro, então o processo simulado teve menos erros do que o processo original, implicando
	que o processo original pode ser melhorado.

	da mesma forma, se quiser avaliar a tarefa "Avalia Contato"

	outliers[outliers.columns[5]].value_counts()[True] < np.max(process['Instances completed']) - process['Instances completed'][5]
"""

def check_errors(df, level, task_index=0, size=300):
	error_vec = []
	for i in range(0, size):
		np.random.seed(i)
		prc_data = generate_data(df)
		outliers = check_outlier(prc_data, level)
		try:
			errors = int(outliers[outliers.columns[task_index]].value_counts()[True])
		except KeyError:
			errors = 0
		error_vec.append(errors)
	comparative = int(np.max(process['Instances completed']) - process['Instances completed'][task_index])
	tstat, pval = atest(error_vec, comparative)
	if pval < 0.01:
		h1 = 'Rejeita H0: Médias Diferentes'
	else:
		h1 = 'Aceita H0: Médias Iguais'
	return {'Estatística do teste: ': tstat, 
			'Média Erros': np.mean(error_vec),
			'Média var2': comparative,			
			'P-Valor: ': pval, 
			'Resultado: ': h1}

check_errors(process, 2)
check_errors(process, 3)
check_errors(process, 4)