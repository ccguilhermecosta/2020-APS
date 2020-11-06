#Definindo o encode do programa para UTF-8
# -*- coding: utf-8 -*-

"""
    Algorítmo Insertion Sort
    Developed by Guilherme Costa and Kauan Polin and Luis Eduardo
"""

#Importando a biblioteca de número randomica
import random
import time

#Menu para escolha da quantidade de dados a serem ordenados
print('------------QUANTIDADE DE NÚMEROS PARA ORDENAR------------')
print('1.000 - Digite 1')
print('50.000 - Digite 2')
print('100.000 - Digite 3')
auxiliar = input('Digite uma opção: \n')

#Definição da varíavel que irá gerar os números randomicos
if auxiliar == 1:
    x = 1000
elif auxiliar == 2:
    x = 50000
else :
    x = 100000


#Definição do Array randomico para ser utilizado na ordenação - Range (Qual será o intervalo de número sorteados) - x (Quantidade de números)
saida = random.sample(range(1000000),  x)

#Printando o Array sem ordenação
print("Tamanho do Array Escolhido")
print(len(saida))
print("\n")
print("Array sem ordenação \n")
print(saida)
print("\n")
print("\n")

#Definição da função de Bubble Sort
def bubbleSort(saida):
    n = len(saida) #Define a varíavel que irá contar o tamanho do array de saída
    for i in range(n - 1): #Laço de repetição que irá funcionar enquanto o índice i tiver o valor do range do array
        flag = 0 #Define uma flag auxiliar igual a 0
        for j in range(n - 1): # Define um segundo for que irá rodar enquanto o índice j tiver o valor do range do array
            if saida[j] > saida[j + 1]: #Se o índice do segundo for for maior que o índice + 1 irá prosseguir no teste
                tmp = saida[j] #Define a varíavel tmp como o valor currente no índice do array saída
                saida[j] = saida[j + 1] # Define o array Saída como o índice +1
                saida[j + 1] = tmp #Define que o índice + 1 do array saída é igual a varíavel auxiliar tmp
                flag = 1 #Define a flag como 1
        if flag == 0: # Se a flag for igual a zero irá parar o programar
            break #Para a execução
    return saida #Retorna o array de saída

print("Array Ordenado \n")
print(bubbleSort(saida)) #Printa o array ordenado
