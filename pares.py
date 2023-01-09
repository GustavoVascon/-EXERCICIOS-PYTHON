#Faça um programa que leia um vetor de 20 inteiros, conte quantos 
#números pares estão contidos no vetor e imprima essa quantidade 
#bem como todo o vetor de números.

numeros = [0]*20
par = 0
impar = 0
qtd = 0
for i in range(20):
        numeros[i] = int(input('Informe os números: '))
        if i % 2 == 0: 
            par += 1
            impar += 1
            qtd = qtd +2
print("Foram alocados no total de {} números".format(qtd))            
print("Existem {} pares".format(par)) 
print("Existem {} ímpares".format(impar))
