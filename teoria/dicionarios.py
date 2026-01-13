'''
Dicionário é muito parecido com tupla e lista, mas é possivel personalizar os indices
'''
'''
dados = {'nome': 'Luiza', 'idade': 20}
print(dados['nome'])
print(dados['idade'])                 
dados['sexo'] = 'F'
del dados['idade']
print(dados)

'''
'''

filme = {
    'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'
}

#print(filme.keys()) indices
# print(filme.values()) valor
#print(filme.items()) os dois

for k, v in filme.items():
    print(f'O {k} é {v}')
'''

pessoas = {
    'nome': 'Luiza', 'idade': 20, 'sexo': 'F'
}
print(pessoas)
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')
pessoas['peso'] = 55
del pessoas['sexo']

print('-' * 60)
brasil = []
estado1 = {'uf' : 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf' : 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
print('-' * 60)

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)