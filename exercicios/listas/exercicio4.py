'''
Crie um programa que:

Tenha uma lista chamada galera.

Dentro dela, cada pessoa será representada por uma sublista com [nome, idade].

Cadastre pelo menos 3 pessoas.

Mostre todos os dados cadastrados.

Mostre apenas os nomes das pessoas.

Calcule e mostre a média das idades.

Mostre quem é maior de idade (idade ≥ 18) e quem é menor de idade.
'''

galera = [['Anna', 25], ['Patrícia', 26], ['Laura', 30]]
print(galera)
print('-' * 70)
print(f'As idades são: {galera[0][1]}, {galera[1][1]}, {galera[2][1]}')
print('-' * 70)
m = ((galera[0][1]) + (galera[1][1]) + (galera[2][1]))/3
print(f'A média das idades é {m}')
print('-' * 70)
print('Todas são maiores de idade')