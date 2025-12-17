# Faça um programa que leia um ângulo qualquer e devolva o seno, cos e tan do ângulo
from math import sin, cos, tan, radians

a = int(input('Digite um ângulo: '))
radians(a)
print('O seno, cosseno e tangente do ângulo informado é {:.2f}, {:.2f} e {:.2f} respectivamente '.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))