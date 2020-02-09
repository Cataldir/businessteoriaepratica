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


leads = pd.read_excel("Campanhas.xlsx", sheet_name="Leads", delimiter=",")
leads_web = leads.loc[0:7]
leads_impresso = leads.loc[8:11]
leads_eventos = leads.loc[12:16]

receita = pd.read_excel("Campanhas.xlsx", sheet_name="Receita", delimiter=",")
receita_web = receita.loc[0:7]
receita_impresso = receita.loc[8:11]
receita_eventos = receita.loc[12:16]

# Taxa média de conversão de grupos de canais
leads_web.mean(axis=1).mean()
leads_impresso.mean(axis=1).mean()
leads_eventos.mean(axis=1).mean()

# Avaliando a relação entre os canais
ro.globalenv["web"] = ro.FloatVector(leads_web.sum(axis=0).to_list()[1:])
ro.globalenv['impresso'] = ro.FloatVector(leads_impresso.sum(axis=0).to_list()[1:])
ro.globalenv['eventos'] = ro.FloatVector(leads_eventos.sum(axis=0).to_list()[1:])

reg1 = stats.lm('impresso ~ web')
print(base.summary(reg1))

reg2 = stats.lm('eventos ~ web')
print(base.summary(reg1))

reg3 = stats.lm('impresso ~ eventos')
print(base.summary(reg1))

# Avaliando retorno de canais
receita_web.mean(axis=1).mean()
receita_impresso.mean(axis=1).mean()
receita_eventos.mean(axis=1).mean()
