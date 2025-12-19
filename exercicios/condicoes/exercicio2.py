#  Escreva um programa que leia a velocidade de um carro, e se passar de 80 tem uma multa de 7 a cada km

vel = int(input('Qual a velocidade do seu carro? (Km/h) '))
if(vel > 80):
    multa = (vel - 80) * 7
    print('Você está acima da velocidade permitida. Sua multa será de R$', multa)
else:
    print('Você está dentro do permitido! ')