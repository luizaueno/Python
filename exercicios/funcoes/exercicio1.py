# faça um programa que tenha uma função chamada area que receba largura e altura e mostre a area

def area(l, c):
    a = l * c
    print(f'A área do terreno de {l} m por {c} m tem {a} m²')


print('Controle de terrenos')
print('-' * 20)
l = float(input('Digite a largura do terreno em m: '))
c = float(input('Digite o comprimento do terreno em m: '))
area(l, c)
