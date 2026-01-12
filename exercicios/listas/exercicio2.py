'''
Leia números até o usuário decidir parar.
Cada número representa o ID de um dispositivo.
Não permita IDs repetidos.
No final, mostre a lista ordenada.
'''
numeros = []
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    if n in numeros:
        print('Não é permitido IDs iguais')
    else:
        numeros.append(n)
print(f'IDs inseridos: {numeros}')