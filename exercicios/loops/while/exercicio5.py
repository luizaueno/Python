# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.



numero = int(input('Digite um número: '))
soma = numero
maior = numero
menor = numero
cont = 1
resposta  = input('Deseja continuar?[s/n] '.lower())

while resposta == 's':
    numero = int(input('Digite um número: '))
    resposta  = input('Deseja continuar?[s/n] '.lower())
    soma += numero
    cont += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
media = soma/cont

print('A media é {:.2f}'.format(media))
print('o maior número é {}'.format(maior))
print('o menor numero é {}'.format(menor))



