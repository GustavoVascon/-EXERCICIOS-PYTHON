while True:
    r = int(input("Digite sua frequência cardíaca em repouso: "))
    f = int(input("Digite sua frequência cardíaca atual: "))
    c = int(input("Digite sua capacidade de oxigenação: "))
    if f >= 35 and f <= 200 and c >= 50 and c <= 100 and r >= 35 and r <= 100:
        diminuir = 3*r
        aumentar = 2*r
        if f > diminuir or c < 95:
            print("diminuir")
        elif f < aumentar and c > 97:
            print("aumentar")
        else:
            print("manter")