# Peça a distancia da viagem em Km e cobre pela passagem: 0.50 por km até 200 e 0.45 para mais

d = int(input('Qual a distância total da sua viagem? '))

if( d <= 200):
   p =  0.50 * d
   print('O preço da passagem é R$ {:.2f}'.format(p))
else:
   p = 0.45 * d
   print('O preço da passagem é R$ {:.2f}'.format(p))