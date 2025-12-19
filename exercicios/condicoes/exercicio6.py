#  leia 3 numeros mostre o menor e o maior


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1

if n2 < n3 and n2 > n3:
    maior = n2
if n3 > n2 and n2 < n3:
    maior = n3

menor = n1

if n2 > n3 and n2 < n3:
    menor = n2
if n3 < n2 and n2 > n3:
    menor = n3

print('O maior número é: {} '.format(maior))
print('O menor número é: {}' .format(menor))