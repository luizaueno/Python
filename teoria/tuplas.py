# tuplas sao imutáveis, não se pode mudar no meio do programa
# python ignora o ultimo número
'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') 
for comida in lanche:
    print(f'Eu vou comer {comida}')
    print(sorted(lanche)) # coloca em ordem alfabética
print('Comi muito')
'''

'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') 
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi muito')
'''
'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') 
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer comida na posição {pos}')
print('comi muito')
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # junta as duas, não soma
d = b + a 
print(d)
print(d.index(5, 1)) # comece no indice 1
#print(len(c))
pessoa = ('Luiza', 20, 'F', 55)
del(pessoa) # para apagar a tupla inteira