# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o us.uário digitar o valor 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
cont = 1
s = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = n + n
cont += 1
print(f'{cont} números foram inseridos')
print(f'{s} é a soma total entre os números')
