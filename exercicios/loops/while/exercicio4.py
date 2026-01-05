#  Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120.
n = int(input('Digite um número: '))

resultado = 1
fatorial = n

while fatorial != 1:
    resultado = resultado * fatorial
    fatorial = fatorial - 1
print('O fatorial de {} é {} '.format(n, resultado))