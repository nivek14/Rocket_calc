# version 1.0

import csv
import math

# função para calcular a taxa.
def calc_taxa(mf,msp,tq):
    return ((mf - msp) / tq)

# criando uma lista para cada tipo de dado da tabela.(usando apenas as colunas necessárias para o cálculo).
tempo = []
accx = []
accy = []
accz = []
vet_aceleracao = [] # vetor para armazenar os valores da aceleração.
vet_massa = [] # vetor para armazenar os valores dos dados de massa.

print('BASE DE DADOS:\n', end="\n")
# abrindo o arquivo csv e colocando os valores de cada dado em sua respectiva lista criada acima.
with open('data_baseex.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for lin in reader:
        time,x,y,z = lin
        tempo.append(float(time)) # atribuindo os dados do tempo da base de dados na lista tempo[].
        accx.append(float(x))     # atribuindo os dados da aceleração em x da base de dados na lista accx[].
        accy.append(float(y))     # atribuindo os dados da aceleração em y da base de dados na lista accy[].
        accz.append(float(z))     # atribuindo os dados da aceleração em z da base de dados na lista accz[].
        print(lin)
file.close()

print('\n', end="\n")


# pegando valores da taxa e realizando o cálculo.
print('-------------------------- VALORES DA TAXA ------------------------------')

print('Valor da massa Final: ', end="")
massa_final = float(input())

print('Valor da massa sem propelente: ', end="")
massa_semprop = float(input())

print('Valor do tempo de queima: ', end="")
temp_queima = float(input())

result_taxa = calc_taxa(massa_final,massa_semprop,temp_queima)

print('Resulatado da taxa: {:.4f}'.format(result_taxa), end="\n")

print('-------------------------------------------------------------------------\n', end="")

# calculando a próxima massa
print('-------------------------- PROXIMA MASSA ------------------------------')
print('Valor da Massa: ', end="")
massa = float(input())
vet_massa.append(massa) # passando os valores da massa para o vetor.
for i in range(0, len(accx)):
    new_massa = vet_massa[i] * result_taxa
    vet_massa.append(new_massa)

print(vet_massa)

print('-------------------------------------------------------------------------\n', end="")

# calculo da aceleração.
print('-------------------------- CALCULANDO ACELERAÇÃO ------------------------')
for i in range(0, len(accx)):
    aceleracao = math.pow(accx[i], 2) + math.pow(accy[i], 2) + math.pow(accz[i], 2)
    aceleracao = math.sqrt(aceleracao)
    vet_aceleracao.append(aceleracao) # passando os valores da aceleração para o vetor
    print('Aceleração({}) = {:.4f}'.format(i,aceleracao), end="\n")
print('-------------------------------------------------------------------------\n', end="\n")

# calculo da força.
print('-------------------------- CALCULANDO FORÇA -----------------------------')
for i in range(0, len(vet_aceleracao)):
    forca = vet_massa[i] * vet_aceleracao[i]
    print('Força({}) = {:.4f}\n'.format(i,forca), end="\n")
print('-------------------------------------------------------------------------\n', end='\n')
