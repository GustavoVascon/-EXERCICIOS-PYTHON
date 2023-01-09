#1.	Faça um programa que leia uma matriz 3x3 e ao final imprima a soma de seus elementos.

soma = 0
ma = [[0]*3,[0]*3,[0]*3]
for lin in range(3):
	for col in range(3):
		ma[lin][col] = int(input('Digite o número: '))
		soma = soma + ma[lin][col]
print(ma)
print(soma)