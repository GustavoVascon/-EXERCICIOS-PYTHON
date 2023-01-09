#B)
n = int(input('Digite um número: '))
for i in range(1, n): 
    for j in range(0, n-i+1): 
        print(' ', end='') 
    C = '*'
    for j in range(1, i+1): 
        print(' ', C, sep='', end='') 
    print() 