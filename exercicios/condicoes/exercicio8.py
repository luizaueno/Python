# leia 3 retas e diga se pode formar um triangulo

r1 = int(input('Diga o valor da primeira reta (cm): '))
r2 = int(input('Diga o valor da segunda reta (cm): '))
r3 = int(input('Diga o valor da terceira reta (cm): '))

if(r1 + r2 > r3):
    print('É possivel formar um triângulo! ')
else:
    print('Não é possível formar um triângulo ')