# Leia o ano de nascimento de um jovem e diga se ainda falta tempo, se é a hora exata ou se já passou da hora de se alistar. deve mostrar o tempo que falta ou que passou

ano = int(input('Digite o ano que você nasceu: '))
ano_atual = 2025
ano_alistamento = ano_atual - ano

if(ano_alistamento < 18):
    ano_ideal = 18 - ano_alistamento
    print('Faltam {} anos para você se alistar'.format(ano_ideal))
elif(ano_alistamento == 18):
    print('Esse é o ano ideal para você se alistar')

else:
    ano_ideal = ano_alistamento - 18
    print('Deveria ter se alistado antes. Já se passaram {} anos'.format(ano_ideal))