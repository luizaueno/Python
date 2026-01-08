'''
1. Simular leituras de temperatura (pode ser um número aleatório dentro de uma faixa, por exemplo, 20°C a 40°C).
2. Repetir a leitura várias vezes (ex: 10 vezes), usando um laço de repetição.
3. A cada leitura, mostrar o valor da temperatura.
4. Se a temperatura passar de um limite (ex: 30°C), mostrar uma mensagem de “ALERTA: Temperatura alta!”.
5. No final, mostrar quantas vezes o alarme foi disparado.
'''
'''
cont = 0
for t in range(1,6):
    temp = float(input('Informe a temperatura de sua sala: '))
    print(f'A temperatura atual é de {temp}ºC')
    if temp > 30:
        cont += 1
        print('ALERTA! Temperatura alta! ')
print(f'O alarme disparou {cont} vezes')
'''
'''
cont = 0
leituras = 0
temp = float(input('Digite a temperatura atual da sala: '))
print(f'A temperatura atual é de {temp}ºC')
while leituras < 11:
    temp = float(input('Digite a temperatura atual da sala: '))
    print(f'A temperatura atual é de {temp}ºC')
    leituras += 1
    if temp > 30:
        cont += 1
        print('ALERTA! Temperatura alta!')
print(f'O alarme disparou {cont} vezes')

'''
leituras = 0
cont = 0
temp = int(input('Digite a temperatura atual da sala: '))
print(f'A temperatura é {temp} ºC')
while leituras < 4:
    temp = int(input('Digite a temperatura atual da sala: '))
    print(f'A temperatura é {temp} ºC')
    leituras += 1
    if temp > 30:
        cont += 1
        print('ALERTA! Temperatura alta!')
    if leituras == 4:
        break
print(f'O alarme disparou {cont} vezes')

