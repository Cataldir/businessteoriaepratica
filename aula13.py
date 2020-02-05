# Importamos a biblioteca numpy para azer os cálculos de distribuição

import random
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Definimos um conjunto de médias, apenas para gerar dados de mesma distribuição

MeanCamis = 30
SigmCamis = 10

MeanBiju = 20
SigmBiju = 5

MeanCalc = 50
SigmCalc = 15

MeanBlus = 30
SigmBlus = 7.5

random.seed(a=100)

# Geramos uma amostra aleatória para cada um dos produtos que estamos vendendo:

vendCam = np.random.lognormal(mean=math.log(MeanCamis), sigma=math.log(SigmCamis), size=100)
bijuRel = np.random.lognormal(mean=math.log(MeanBiju), sigma=math.log(SigmBiju), size=100)

vendBiju = np.add(vendCam, bijuRel)

vendCalc = np.random.lognormal(mean=math.log(MeanCalc), sigma=math.log(SigmCalc), size=100)
blusRel = np.random.lognormal(mean=math.log(MeanBlus), sigma=math.log(SigmBlus), size=100)

vendBlus = np.add(vendCalc, blusRel)

# concatenamos os dados em um único dataframe

vendasPD = pd.DataFrame(list(zip(vendCam, vendBiju, vendCalc, vendBlus)), 
	columns=['Camisetas', 'Bijuterias', 'Calças', 'Blusinhas'])

# Padronizamos os dados (Veremos sobre padronização em aulas futuras)

vendasPadr = StandardScaler().fit_transform(vendasPD)

# e então geramos os componentes e seu dataframe

vendasPCA = PCA(2)
vendasComponents = vendasPCA.fit_transform(vendasPD)
vendasVariance = vendasPCA.fit(vendasPD).explained_variance_ratio_

principalDf = pd.DataFrame(data = vendasComponents, 
	columns = ['principal component 1', 'principal component 2'])

# por fim, criamos um data frame completo para avaliar a correção

finalDF = vendasPD.join(principalDf)
mtr_cor = finalDF.corr()

sn.heatmap(mtr_cor, annot=True)
plt.show()
