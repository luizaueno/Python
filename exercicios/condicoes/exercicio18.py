# crie um programa para jogar jokenpô com o usuario

import random
opcoes = ['pedra', 'papel', 'tesoura']
escolha1 = random.choice(opcoes)
escolha2 = str(input('Escolha entre pedra, papel ou tesoura: ')).lower().strip()

print('Eu escolhi {} e você escolheu {}'.format(escolha1, escolha2))

if escolha1 == escolha2:
    print('Empate!')
elif escolha1 == 'papel' and escolha2 == 'tesoura':
    print('Você ganhou!')
elif escolha1 == 'tesoura' and escolha2 == 'papel':
    print('Eu ganhei!')
elif escolha1 == 'pedra' and escolha2 == 'papel':
    print('Você ganhou!')
elif escolha1 == 'papel' and escolha2 == 'pedra':
    print('Eu ganhei!')
elif escolha1 == 'pedra' and escolha2 == 'tesoura':
    print('Eu ganhei!')
elif escolha1 == 'tesoura' and escolha2 == 'pedra':
    print('Você ganhou!')
else:
    print('Jogada inválida! Digite pedra, papel ou tesoura.')

