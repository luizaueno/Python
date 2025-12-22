# Refaça o exercicio 35 e mostre se é equilatero 3=; isosceles 2=; escaleno 3!=

l1 = int(input('Digite o valor do lado 1: '))
l2 = int(input('Digite o valor do lado 2: '))
l3 = int(input('Digite o valor do lado 3: '))

if l1  == l3:
    print('Esse triângulo é equilátero ')
elif l1 == l2:
    print('Esse triângulo é isosceles ')
elif l1 != l2 != l3:
    print('Esse triângulo é escaleno')