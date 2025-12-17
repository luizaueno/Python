# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. h² = co² + ca²

import math

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('O comprimento da hipotenusa vale: {}'.format(math.hypot(co,  ca)))
