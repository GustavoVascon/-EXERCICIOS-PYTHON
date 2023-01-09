#Listar os 20 primeiros números da serie de Fibonacci

anterior = 0
proxima = 1
soma = 1

for i in range(0, 21):
    print(anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma


