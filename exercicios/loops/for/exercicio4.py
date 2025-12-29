# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


num = int(input('Escolha um número: '))
print('A tabuada de {} é: '.format(num))

for i in range(1, 11):
   r =  num * i
   print('{} x {} = {} '.format(num, i, r))

numero = int(input('Escolha um número: '))
print('A tabuada de {} é: '.format(numero))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print('{} x {} = {}'.format(numero, multiplicador, resultado))

