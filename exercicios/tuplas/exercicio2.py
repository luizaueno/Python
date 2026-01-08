# Crie uma tabela preenchida com os 20 primeiros colocados na tabela do brasileirao e mostre:
# apenas os 5 primeiros
# os 4 ultimos
# ordem alfabética
# em que posição está chapecó

times = ('Atlético mineiro', 'Botafogo', 'Atlético Paranaense', 'Chapecoense', 'Coritiba', 'Flamengo', 'Vasco', 'Cruzeiro', 'Bahia', 'EC Vitória', 'Fluminense', 'Geêmio', 'Mirassol', 'Bragantino', 'Remo', 'Santos', 'São Paulo', 'Corinthians', 'Internacional', 'Palmeiras')

print('-' * 100)
print('Os 5 primeiros são' , times[:5])
print('-' * 100)
print('Os 4 últimos são', times[-4:])
print('-' * 75)
print('Em ordem alfabética: ', sorted(times))
print('-' * 124)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
print('-' * 36)