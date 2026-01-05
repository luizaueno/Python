# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

g = str(input('Diite seu gênero [M / F]: ').upper())

if g != 'M' and g != 'F':
    print('Tente de novo! ')
    while  g != 'M' and g != 'F':
        g = str(input('Diite seu gênero [M / F]: ').upper())

print('Seu gênero é: {}'.format(g.upper()))
