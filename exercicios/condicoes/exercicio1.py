# Faça o computador pensar em um número entre 0 e 5 e o usuário advinhar. dizer se acertou ou errou
import random

num =  int(input('Pensei em um número entre 1 e 5, tente advinhar! '))
num2 = random.randint(1,5)

if (num == num2):
    print('Parabéns! Você acertou!')
else:
    print(f'Errou, o número era: ',  {num2})