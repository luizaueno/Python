'''
Imagine que você precisa criar um sistema de cadastro de funcionários.
Cada funcionário terá:

Nome

Cargo

Salário

 O sistema deve permitir:

Cadastrar funcionários em um dicionário.

Consultar dados de um funcionário específico.

Calcular a média salarial de todos os cadastrados.
'''

funcionarios = [{'Nome': 'José', 'Cargo': 'Desenvolvedor júnior', 'Salário': '3000'}, {'Nome': 'Paulo', 'Cargo': 'Desenvolvedor pleno', 'Salário': '7000'}]
print(funcionarios)
funcionarios.append({'Nome':'Bernardo', 'Cargo': 'Desenvolvedor senior', 'Salário': '20000'})
print(funcionarios)
print(funcionarios[1])
print('-' * 60)
s = 0
for f in funcionarios:
    s += int(f['Salário'])
    m = s/len(funcionarios)
print(f'A média salarial é {m}')