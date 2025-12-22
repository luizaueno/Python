# Leia um número inteiro qualquer e peça para o usuário escolher entre 1- para binário, 2- para octal e 3- para hexadecimal. bin(numero) [2:] oct e hex

valor = int(input('Digite um valor inteiro: '))
escolha = int(input('Transforme em binário, octal ou hexadecimal. Digite [1] [2] ou [3] respectivamente: '))

if escolha == 1:
    binario = bin(valor)[2:]
    print('O valor {} em binário é {} '.format(valor, binario))
elif escolha == 2:
    octal = oct(valor)[2:]
    print('O valor {} em octal é {}'.format(valor, octal))
elif escolha == 3:
    hexadecimal = hex(valor)[2:]
    print('O valor {} em hexadecimal é {}'.format(valor, hexadecimal))
else:
    print('Digite um valor válido! 1 2 ou 3')