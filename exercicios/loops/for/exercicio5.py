# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for n in range(1, 7):
    num = int(input('Digite um número: '))
    if(num % 2 == 0):
        soma += num
    else:
        print('Não é possivel realizar soma de números ímpares')

print('A soma dos números é {}'.format(soma))

for cont in range (1, 7):
    numero = int(input('Digite um número: '))

    if(numero % 2 == 0):
        soma = soma + numero
        
    else: 
        print('Os valores ímpares não podem ser somados ')

print('A soma dos valores digitados é: {}'.format(soma))


