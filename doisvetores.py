#Faça um programa que lê 10 números inteiros e os armazena em um 
#vetor, e calcula e mostra dois vetores resultantes:
#o primeiro vetor resultante deve conter os números positivos;
#o segundo deve conter os números negativos.

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