'''
Crie uma lista vazia.
Leia 5 valores numéricos e armazene na lista.
No final, mostre todas as leituras.

Mostre o maior valor

Mostre o menor valor

Mostre a posição de cada um

'''
numeros = []


for n in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
print(f'Números da lista: {numeros}')

maior = numeros[0]
menor = numeros[0]
pos_maior = 0
pos_menor = 0
for pos, n in enumerate(numeros):
    if n > maior:
        maior = n
        pos_maior = pos
    if n < menor:
        menor = n
        pos_menor = pos
print(f'Maior número {maior} na posição {pos_maior}')
print(f'Menor número {menor} na posição {pos_menor}')