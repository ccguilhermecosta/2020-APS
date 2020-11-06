#Definindo o encode do programa para UTF-8
# -*- coding: utf-8 -*-

"""
    Algorítmo Insertion Sort
    Developed by Guilherme Costa and Kauan Polin and Luis Eduardo
"""

#Importando a biblioteca de número randomica
import random

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
array = random.sample(range(1000000),  x)

#Printando o Array sem ordenação
print("Tamanho do Array Escolhido")
print(len(array))
print("\n")
print("Array sem ordenação")
print(array)

#Definindo a função de Ordenação
def insertionSort(array):
    for p in range(0, len(array)): #Laço de repetição para começar a ordenar
        current_element = array[p] #Definição da varíavel Current que é o índice currente do array

        while p > 0 and array[p - 1] > current_element: #Enquanto o índice for maior que zero e o valor anterior do array for maior que o elemento currente, irá continuar no laço
            array[p] = array[p - 1] #Irá definir que a posição do array será o número anterior
            p -= 1 #Define o índice do array para diminuir 1 valor

        array[p] = current_element #Adiciona o elemento que está no current_element ao array

insertionSort(array) #Chama a função de Insertion

print("Array Ordenado")
print("\n")
print("\n")
print(array) #Printa o Array Ordenado
