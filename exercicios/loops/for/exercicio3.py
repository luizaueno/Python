# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for n in range (1, 501):
    if(n % 2 != 0 and n % 3 == 0):
        soma += n
print(soma)

for impares in range (1, 501):
    if(impares % 2 != 0 and impares % 3 == 0):
        soma += impares
print('A soma de todos os números impares e multíplos de 3 no intervalo de 1 a 500 é: {}'.format(soma))
