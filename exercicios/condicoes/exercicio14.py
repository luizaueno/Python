# Leia o ano de nascimento de um atleta de natação e mostre sua categoria de acordo com a idade: até 9 anos mirim; ate 14 infantil; ate 19 junior; até 25 senior; acima de 25 master 

idade = int(input('Quantos anos você tem? '))
if idade <= 9:
    print('Você está na categoria mirim ')
elif idade  <= 14:
    print('Você está na categoria infantil')
elif idade  <= 19:
    print('Você está na categoria junior')
elif idade <= 25:
    print('Você está na categoria senior')
else:
    print('Você está na categoria master')