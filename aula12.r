# Definindo o tempo e o consumo do forno atual, em média e desvio padrão

muConsAtual = 5
dpConsAtual = 10

muTempAtual = 20
dpTempAtual = 5

#----#
# Definindo o tempo e o consumo do novo forno, em média e desvio padrão

muConsNovo = (muConsAtual-muConsAtual*0.3)
dpConsNovo = dpConsAtual

muTempNovo = (muTempAtual-muTempAtual*0.2)
dpTempNovo = dpTempAtual

#----#
# Para fins didáticos, consideraremos uma função de distribuição Log Normal.
dist_cons_atual = rlnorm(365, meanlog = log(muConsAtual), sdlog = log(dpConsAtual))

dist_temp_atual = rlnorm(365, meanlog = log(muTempAtual), sdlog = log(dpTempAtual))

dist_cons_novo = rlnorm(365, meanlog = log(muConsNovo), sdlog = log(dpConsNovo))

dist_temp_novo = rlnorm(365, meanlog = log(muTempNovo), sdlog = log(dpTempNovo))


#----#
# Agora, é hora dos testes. Basta fazer um teste T para avaliar se a média entre as duas condições 
# é estatisticamente igual, e aí teremos evidência para dizer se existe ou não melhora de custos
# que justifique a mudança de fogão.

t.test(dist_cons_atual, dist_cons_novo)
t.test(dist_temp_atual, dist_temp_novo)