#Elabore um programa em Python que leia 2 vetores com 5 valores 
#inteiros cada e determine o vetor soma.

vetor1 = [0]*3
vetor2 = [0]*3
soma =  [0]*5
for i in range(3):
        vetor1[i] = int(input('Informe os números do i: '))
for i in range(3):
        vetor2[i] = int(input('Informe os números do o: '))
for i in range(3):
        soma[i] = vetor1[i] + vetor2[i]
print(vetor1)
print(vetor2)
print(soma)
print([vetor1[0] + vetor2[0], vetor1[1] + vetor2[1], vetor2[2] + vetor1[2]])

