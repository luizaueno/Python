# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for n in range(1, 7):
    num = int(input('Digite um número: '))
    if(num % 2 == 0):
        soma += num
    else:
        print('Não é possivel realizar soma de números ímpares')

print('A soma dos números é {}'.format(soma))