# Suponha que você precise fazer um programa para cadastrar
# as notas de 20 alunos de uma determinada turma, calcular a
# média da turma e contabilizar quantos alunos tiveram nota
# acima da média da turma. Como você resolveria essa
# situação?

notas = [0.0]*20
qtde = 0
media = 0.0
for i in range(20):
    notas[i] = float(input("Informe a nota: "))
    media = media + notas[i]
# Calcula a media
    media = media / 20
# Faz a contagem de quantas notas ficaram acima da média.
for i in range(20):
    if (notas[i] > media):
        qtde = qtde + 1
        print('Média: {}'.format(media))
        print('Notas acima da média: {}'.format(qtde))
