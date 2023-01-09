#3.	Construa um programa que leia uma matriz 4x4 e calcule e imprima a soma da diagonal principal

soma = 0
ma = [[0]*4, [0]*4, [0]*4, [0]*4]
for lin in range(4):
    for col in range(4):
        ma[lin][col] = int(input('Digite o número: '))
print(ma)
print(ma[0][0] + ma[1][1] + ma[2][2] + ma[3][3])


