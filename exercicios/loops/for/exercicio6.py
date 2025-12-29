# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão dessa P.A: '))
print('Os 10 primeiros termos de uma PA são: ')

for passo in range(10):
    t = (p + (passo * r)) 
    print(t, end= ' ')