'''
Crie um programa que tenha uma tupla com 7 temperaturas (valores reais), representando a temperatura de cada dia da semana.

O programa deve:

Mostrar todas as temperaturas

Mostrar a maior e a menor temperatura

Mostrar a média das temperaturas

Informar em quais posições ocorreram temperaturas acima de 30°C
'''
print('-' *60)
cont = ''
temp =(24, 25, 30, 32, 30, 29, 31)
print(f'Temperaturas durante a semana: {temp}')

print('-' *60)

menor = temp[0]
maior = temp[0]
for t in temp:
    if t < menor:
        menor = t
    if t > maior:
        maior = t
print(f'A maior temperatura foi: {maior} e a menor foi: {menor}')

print('-' *60)

s = 0
for t in temp:
    s = s + t
media = s/len(temp)
print(f'A média das temperaturas foi {media:.2f}')

print('-' *60)

cont = 0
posicoes = ''
for pos, t in enumerate(temp):
    if t > 30:
        cont += 1
        if cont == 1:
            posicoes += f'{pos + 1}'
        else:
            posicoes += f' e {pos + 1}'

print(f'Temperaturas acima de 30º ocorreram nas posições {posicoes}')
print('-' * 60)