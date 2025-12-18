# crie um programa que leia o nome da cidade e diga se começa ou nao com santo
cidade = input('Digite o nome da sua cidade: ').strip()
print(cidade[:5].upper() == 'Santo')