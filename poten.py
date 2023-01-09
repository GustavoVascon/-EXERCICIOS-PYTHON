#Faça um programa que leia dois valores representando a base e o expoente de uma potência. 
# você deve implementar uma função que computa a potência ab para valores a e b (assuma números inteiros) passados por parâmetro.

def potencia(a,b):
    if b == 0:
        return 1
    return (a*potencia(a, b-1))
n1 = int(input("Informe o valor da base: "))
n2 = int(input("Informe o valor do expoente: "))
resposta = potencia(n1,n2)
print(potencia(n1, n2))