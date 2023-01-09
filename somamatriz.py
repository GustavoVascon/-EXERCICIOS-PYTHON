soma = [0]
matriz = [[0]*3, [0]*3, [0]*3]
for lin in range(3):
    for col in range(3):
        matriz[lin][col] = int(input('Digite os números: '))
        soma = matriz[lin][col] + soma
        print(soma)