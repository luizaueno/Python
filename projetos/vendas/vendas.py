'''
- Tenha uma **tupla** com **7 valores numéricos** representando vendas diárias.
- Mostre:
    - todas as vendas
- Calcule e mostre:
    - o **total de vendas da semana**
    - a **média diária**
- Mostre:
    - **quantos dias** tiveram vendas **acima de R$ 1.000**
- Mostre:
    - **em qual posição ocorreu a maior venda**
- Se existir uma venda **exatamente igual a R$ 500**, informe:
    - a **posição da primeira ocorrência**
    - se não existir, informe isso claramente
'''
print('-' * 67)
vendas = (2000, 8000, 500, 3000, 4000, 4500, 6000)
print(f'Todas as vendas do dia: {vendas}')
print('-' * 67)
t = 0
for v in vendas:
    t += v
print(f'Total de vendas da semana: {t}')
print('-' * 67)
m = 0
m = t/len(vendas)
print(f'A média diária de vendas foi: {m:.2f}')
print('-' * 67)
cont = 0
for  v in vendas:
    if v > 1000:
        cont += 1
print(f'{cont} dias as vendas foram maiores que mil reais, essa semana')
print('-' * 67)
valor_maior = 0
pos_maior = 0
for pos, v in enumerate(vendas):
   if v > valor_maior:
       valor_maior = v
       pos_maior = pos
print(f' a maior venda da semana ocorreu na {pos_maior +1} posição ')
print('-' * 67)
venda = False
for pos, v in enumerate(vendas):
     if v == 500:
        venda = True
        print(f'A venda com valor de 500 reais aconteceu na {pos +1} posição')
if venda == False:
    print('não teve nenhuma venda com valor 500 hoje')
print('-' * 67)