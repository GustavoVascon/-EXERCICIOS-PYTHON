#Escreva um programa que armazene 10 números inteiros em um 
#vetor e exiba o maior e o menor valor armazenado.

numero_inp = [0]*10
maior = int()
menor = int()

for i in numero_inp:
    numero_inp = int(input('Digite os 10 números: '))
    if numero_inp > maior:
        maior = numero_inp
    if numero_inp < menor:
        menor = numero_inp
print(maior)
print(menor)