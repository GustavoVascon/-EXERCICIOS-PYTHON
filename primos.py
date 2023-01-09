#Um número primo é aquele que é dividido apenas por um e por ele mesmo. 
# Escreva um programa que leia um número inteiro “n” e apresente todos os números primos de 0 a n. 

#Exemplo: 
#N=10 => [2,3,5,7]
#N=23 => [2,3,5,7,11,13,17,19,23]


n = int(input('Digite um número: '))
for i in range(n): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 