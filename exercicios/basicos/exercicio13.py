#  leia o salário e mostre com 15% de aumento
s = float(input('Qual seu salário? '))
ns = s + (s * 0.15)
print('Parabéns! Você ganhou um aumento de 15%. Seu novo salário é: {:.2f}'.format(ns))