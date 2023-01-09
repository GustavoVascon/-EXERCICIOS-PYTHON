# 2.	Escreva um programa que leia uma matriz 3x3, armazene em um vetor a soma dos elementos por linha e exiba a matriz e o vetor de soma.


ma = [[0]*3, [0]*3, [0]*3]
for lin in range(3):
    for col in range(3):
        ma[lin][col] = int(input('Digite o número: '))
soma0 = ma[0][0] + ma[0][1] + ma[0][2]
soma1 = ma[1][0] + ma[1][1] + ma[1][2]
soma2 = ma[2][0] + ma[2][1] + ma[2][2]
print(ma)
print([soma0, soma1, soma2])



