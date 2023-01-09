import math

def seno(x):
    senx = 0
    i = 0
    while True:
        somatório = (-1)**i*((x**(2*i+1))/(math.factorial(2*i+1)))
        senx = senx + somatório
        i = i + 1
        print(senx)
        print(i)
        if somatório < 0.0001:
            print("O valor calculado pela função é: ", (senx))
            break

seno(math.pi/6)

print("O valor calculado pela biblioteca é: ", math.sin(math.pi/6))

