'''
Crie um programa que tenha uma função chamada calcular_media que receba uma lista de notas de um aluno e retorne a média.
Depois, crie outra função chamada situacao_aluno que use a média para dizer se o aluno está aprovado (média ≥ 7) ou reprovado.
'''

def calcular_media(*notas):
    s = 0
    for n in notas:
        s += n
    media = s/len(notas)
    print(f'A média é {media:.2f}')
    return media

def situacao_aluno(*notas):
    m = calcular_media(*notas)
    if m >= 7:
        print('Aprovado')
    else:
        print('Reprovado!')




nota1 = float(input('Informe sua nota 1: '))
nota2 = float(input('Informe sua nota 2: '))
calcular_media(nota1, nota2)
print(situacao_aluno())