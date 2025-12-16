# 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Por quantos dias o carro será alugado? ' ))
km = float(input('Quantos quilômetros foram rodados? '))
preco = (60 * d) + (0.15 * km)
print('O valor total a ser pago é: R$ {:.2f} '.format(preco))