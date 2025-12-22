#  Calcule o valor a ser pago por um produto de acordo com a forma de pagamento: a vista ou cheque = 10%
#  a vista no cartao = 5%
#  2x do cartao = preço normal 3x ou mais = 20% de juros

produto = float(input('Informe o preço do produto: '))
pagamento = float(input('Qual a forma de pagamento? [1] a vista ou cheque; [2] a vista no cartão; [3] 2x no cartão; [4] 3x ou mais parcelado: '))

if pagamento == 1:
    preco = produto - (produto * 0.1)
    print('O valor final será R$ {:.2f}'.format(preco))
elif pagamento == 2:
    preco = produto - (produto * 0.05)
    print('O valor final será R$ {:.2f}'.format(preco))
elif pagamento == 3:
    preco = produto
    print('O valor final será R$ {:.2f}'.format(preco))
else:
    preco = produto + (produto * 0.2)
    print('O valor final será R$ {:.2f}'.format(preco))