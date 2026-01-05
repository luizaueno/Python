#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
n1 = random.randint(1, 10)
n2 = int(input('Tente advinhar o número que pensei: '))
tentativas = 0

while n1 != n2:
    print('Você errou! Mais uma chance.')
    n2 = int(input('Tente advinhar o número que pensei: '))
    tentativas += 1

print('Você acertou depois de {} tentativas'.format(tentativas))