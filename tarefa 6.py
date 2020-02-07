import numpy as np
import pandas as pd

from scipy.stats import ttest_ind as htest
from scipy.stats import ttest_1samp as atest

np.random.seed(100)

# Importe os dados como dataframes do Pandas

dfc_dia = pd.read_excel("Contas Financeiras.xlsx", sheet_name="DFC-Diario", delimiter=",")
dfc_dia = dfc_dia.T
dfc_dia.columns = dfc_dia.iloc[0]
dfc_dia = dfc_dia.drop(dfc_dia.index[0])

dre_dia = pd.read_excel("Contas Financeiras.xlsx", sheet_name="DRE-Diario", delimiter=",")
dre_dia = dre_dia.T
dre_dia.columns = dre_dia.iloc[0]
dre_dia = dre_dia.drop(dre_dia.index[0])

# Para calcular a média e o desvio padrão, utilize o seguinte:

# DFC diário
media_dfc = dfc_dia.mean().to_frame()
std_dfc = dfc_dia.std().to_frame()

# DRE diária
media_dre = dre_dia.mean().to_frame()
std_dre = dre_dia.std().to_frame()

# (Slicing) Para tirar os dados de um determinado trimestre, selecione pelos dias.
# Por exemplo, para o primeiro trimestre:

dfc_dia_T1 = dfc_dia[0:90]
dfc_dia_T2 = dfc_dia[91:180]


# Para realização dos testes de hipótese, utilize o seguinte código:
"""
	Neste código, você vai avaliar uma determinada série. Por exemplo, a série 1 do data frame
	dfc_dia é a receita total (olhe na planilha). Da mesma forma, você pode capturar uma determinada
	quantidade de entradas fazendo um corte no banco de dados.

	por exemplo, se você quiser pegar os 100 primeiros dias da série de receita total, você faz assim:
	dfc_dia[1][0:100]

	para fazer um teste entre o primeiro trimestre (primeiros 90 dias) e o segundo trimestre
	(do dia 91 ao dia 180), você faz assim:

	teste_hip(dfc_data[1][0:90], dfc_data[1][91:180])

	Isso vai te retornar uma lista com o resultado do teste.
"""

def teste_hip(var1, var2, significance=0.01, test_type=htest):
	tstat, pval = test_type(var1, var2)
	if pval < significance:
		h1 = 'Rejeita H0: Médias Diferentes'
	else:
		h1 = 'Aceita H0: Médias Iguais'
	return {'Estatística do teste: ': tstat, 
			'Média var1': var1.mean(),
			'Média var2': var2.mean(),			
			'P-Valor: ': pval, 
			'Resultado: ': h1}

# Por exemplo, para testar a receita total
teste_hip(dfc_dia_T1['Total Receitas'], dfc_dia_T2['Total Receitas'])

# se você quiser testar direto a média, faça o seguinte:
teste_hip(dfc_dia_T1['Total Receitas'], dfc_dia_T2['Total Receitas'].mean(), test_type=atest)

# Se você quiser testar com base em diferentes graus de significância, basta definir o grau:
teste_hip(dfc_dia_T1['Total Receitas'], dfc_dia_T2['Total Receitas'], significance=0.05)