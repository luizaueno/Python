# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a vinte. Ao digitar, deve mostrar por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    if not 0 <= n <= 20:
        print('Tente Novamente.' , end=' ')
        continue

    print(f'Você digitou o número {numeros[n]}')
    
    resposta =  input('Quer continuar? [s/n] ').lower()
    if resposta == 'n':
        break
      