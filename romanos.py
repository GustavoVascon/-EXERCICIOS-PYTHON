def numero_romano(numero):
    inteiro_romano = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    texto_romano = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    retorno = ''
    for i in range(len(inteiro_romano)):
        while numero >= inteiro_romano[i]:
            numero -= inteiro_romano[i]
            retorno += texto_romano[i]
    return retorno
 
 
user_input = int(input('Converta o número para romano: '))
romano_numero = numero_romano(user_input)
print('O número {0} em romano é: {1}'.format(user_input, romano_numero))