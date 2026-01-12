'''
1 - Crie uma lista chamada sensores.

Cada sensor deve ser uma lista com:

[nome_do_sensor, valor_lido]


O programa deve:

Ler o nome e o valor de 3 sensores

Guardar cada sensor dentro da lista sensores

Ao final, mostrar:

Sensores cadastrados: [[...], [...], [...]]
'''
sensor = list()
sensores = list()
for c in range(0, 3):
    sensor.append(str(input('Nome do sensor: ')))
    sensor.append(int(input('Valor do sensor: ')))
    sensores.append(sensor[:])
    sensor.clear()
    print(f'Sensores cadastrados: {sensores}')

cont = 0
for s in sensores:
    if s[1] > 30:
        print(f'Alerta! {s[0]} acima do limite permitido')
        cont += 1
print(f'O alerta foi acionado {cont} vezes')

resposta =str(input('Deseja cadastrar outros sensores:[s/n]? '))
if resposta == 'n':
    print('Sensores Cadastrados com sucesso! ')

while resposta == 's':
    sensor.append(str(input('Nome do sensor: ')))
    sensor.append(str(input('Valor do sensor: ')))
    sensores.append(sensor[:])
    sensor.clear()
    resposta =str(input('Deseja cadastrar outros sensores:[s/n]?'))
print(f'Sensores cadastrados: {sensores}')


