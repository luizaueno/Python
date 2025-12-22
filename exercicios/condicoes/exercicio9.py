# 36- Escreva um programa para aprovar o empréstimo para a compra de uma casa, pergunte o valor da casa, o salário do comprador, e em quantos anos ele pagará. A prestação mensal não pode exceder 30% do salário ou então será negado

casa = float(input('Informe o valor da casa: '))
sal = float(input('Informe seu salário: '))
anos = int(input('Em quantos anos vai financiar? '))

meses = anos * 12  
prestacao = (casa / meses) 
minimo = 0.3 * sal

if(prestacao > (minimo)):
    print('O seu financiamento foi negado ')
else:
    print('O valor mensal de seu financiamento será de R$ {:.2f} '.format(prestacao))