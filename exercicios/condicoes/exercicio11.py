#  Escreva um programa que leia 2 numeros inteiros e compare-os. Mostrando se o primeiro é maior, o segundo ou se não existe os 2 sao iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if(num1 > num2):
    print('{} é maior que {}'.format(num1, num2))
elif(num1 < num2):
    print('{} é menor que {}'.format(num1, num2))
else:
    print('Não existe, os números são iguais ')