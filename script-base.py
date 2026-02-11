# -*- coding: utf-8 -*-
#Teste mini-curso de ML

print(10 + 9)
print("Resultado final da conta.")

result = 10 + 10
print(f"Valor final é: {result}")

result = 30 * 3
print(f"Valor final da multply: {result}")

valor = float(input("Digite o valor:"))
valor2 = float(input("Digite o 2 valor:"))

result2 = valor ** valor2

print(f"Valor final da potência: {result2}")

import numpy as np
import pandas as pd


#Imprimindo a Raiz quadadra de 144.
print(np.sqrt(144))

#Listas
lista_times = ['cruzeiro', 'flamengo', 'corintians']

print(lista_times[0])

valores = [0, 20, 30, 50, 60]

print(valores[0] + valores[4])
print(f"{valores[0]} + {valores[2]}")

result = valores[0] + valores[2]
print(f"Resultado: {result}")

valor = pd.Series([10, 20])

print(valor)

#Importando data-set em excel
titanic = pd.read_excel('titanic.xlsx')

titanic.info()

#Separando apenas uma coluna em específico
sexo_tipo = titanic[['sexo', 'idade']]


print(sexo_tipo)

#Removendo uma coluna de uma variável separada.
sexo_tipo = sexo_tipo.drop(columns=['idade'])

print(sexo_tipo)

#Fazendo separação com operadores lógicos.
sobreviveu = titanic[titanic['sobreviveu'] == 'nao']
print(sobreviveu)

idade = (titanic[(titanic['classe'] == 'primeira') &
                (titanic['idade'] >= 18)])
print(idade)

#Para fazer análises e extrair informações, basta fazer o count.
#Qualitativas = value_counts()
#Quantitativas = count()
titanic['sobreviveu'].value_counts()
titanic['sobreviveu'].value_counts(normalize=True)

titanic['idade'].mean()