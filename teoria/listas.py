# listas podem mudar no meio do programa
'''
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'sorvete'
lanche[4] = 'refri'
lanche.append('cookie')
lanche.insert(0,'cachorro quente')
lanche.remove('pizza')
print(lanche)

valores = [8, 2, 5, 1, 6, 3]
valores.sort() # ordem crescente
valores.sort(reverse=True) # ordem decrescente
len(valores)

'''
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
# num.sort() 
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

'''
'''
valores = []
valores.append(5)
valores.append(9)                
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
'''

a = [2, 3, 4, 7]
b = a 
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')
print('-' * 20)
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')
