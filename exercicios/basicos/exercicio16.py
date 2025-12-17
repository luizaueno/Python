# Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira

import math

n = float(input('Digite qualquer número real: '))
ni = math.trunc(n)
print('O número {} tem a parte inteira {}'.format(n, ni))