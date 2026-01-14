'''
Crie uma tupla chamada agenda que guarda informações de 3 contatos.
Cada contato deve ser representado por uma tupla com:

Nome (string)

Telefone (string)

Idade (inteiro)

Depois, faça um programa que:

Mostre todos os contatos da agenda.

Mostre apenas os nomes dos contatos.

Calcule a média das idades.

Mostre o telefone do segundo contato.
'''

agenda = ("Ana", "985678090", "20", 
          "Débora", "98453211", "22", 
          "Fabricio", "95421345", "18")

print(f'Todos os contatos da agenda são: {agenda}')
print(f' O nome de cada um dos contatos são: {agenda[0]}, {agenda[3]}, {agenda[6]}')
print('-' * 30)
m = (int(agenda[2]) + int(agenda[5]) + int(agenda[8]))/3
print(f'A média das idades é {m:.2f}')
print('-' * 30)
print(f'O tefone do segundo contato é: {agenda[4]}')