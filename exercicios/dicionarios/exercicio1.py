# 1- Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário e mostre na tela

nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media < 7:
    situacao = 'reprovada'
else:
    situacao = 'aprovada'
aluno = {'nome': nome, 'media': media, 'situacao': situacao}
print(f' A Aluna {nome} teve média {media} e está {situacao}!')

