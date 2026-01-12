'''
teste = list()
teste.append('Luiza')
teste.append(20)
print(teste)

galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

galera = [['Luiza', 20], ['Ana', 25], ['Yasmin', 28], ['João', 31]]
print(galera[0] [0])
print(galera[2] [1])
print('-' * 20)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-' * 20)

totmai = 0
totmen = 0
pessoas = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ' )))
    pessoas.append(dado[:]) # coloca a lista de dados em pessoas
    dado.clear() #

for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')