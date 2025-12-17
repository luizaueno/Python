'''
módulos são bibliotecas a mais que podemos adicionar no código, usando import
para importar um específico, escreva from nome_ import outro nome
por exemplo na biblioteca math, tem ceil para arredondar pra cima e floor para arredondar para baixo. trunc elimina da , para frente. pow é potencia(igual a **). sqrt para raiz quadrada e factorial para fatorial.
exemplo: import math ou from math import sqrt ou sqrt, ceil

'''

'''

import math 
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# para from math import sqrt nao precisa do math.
from math import sqrt 
num = int(input('Digite um número: '))
raiz = sqrt(num)
'''

import random
num = random.random()  # ou random.randint(1, 10)
print(num)
