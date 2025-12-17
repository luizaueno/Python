# um professor quer sortear 4 de seus alunos e leia o nome deles aparecendo o nome do escolhido

from random import choice, random

alunos = ['Lara', 'Leonardo', 'Lavínia', 'Levi']

escolhido = choice(alunos)
print('o nome escolhido foi: {} '.format(escolhido))