# -  Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('--------------------')

resposta = int(input('Digite 1 para: somar; 2 para: multiplicar; 3 para saber o maior; 4 para inserir novos; e 5 para sair do programa: '))

while resposta != 5:
    if resposta == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a {}'.format(n1, n2, soma))
    elif resposta == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, multi))
    elif resposta == 3:
        if n1 > n2:
            print('o maior número é: {}'.format(n1))
        else:
            print('o maior número é: {}'.format(n2))
    elif resposta == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
 
    resposta = int(input('Digite 1 para: somar; 2 para: multiplicar; 3 para saber o maior; 4 para inserir novos; e 5 para sair do programa: '))

print('Volte sempre!')

print('--------------------')