def irpf(salario):
    while True:
        if salario >= 1903.99 and salario <= 2826.65:
            aliquota = 7.50
        elif salario >= 2826.66 and salario <= 3751.05:
            aliquota = 15.00
        elif salario >= 3751.06 and salario <= 4664.68:
            aliquota = 22.50
        elif salario >= 4664.68:
            aliquota = 27.50
        elif salario <= 1903.99 and salario >= 0:
            aliquota = 0
        elif salario <= -1:
            print('Saindo do programa...')
            break
        resultado = (salario * aliquota) / 100
        print('Descontada em porcentagem:  {}%'.format(aliquota))
        print('Desconto ganho:           R${}'.format(resultado))
        print('Valor final com desconto: R${}'.format(salario-resultado))
        return resultado

valor_salario = float(input("Valor salário:            R$"))
res = irpf(valor_salario)