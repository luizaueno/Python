# Leia o nome completo de uma pessoa, mostre todas as minusculas, maiusculas, quantas letras sem espaço e quantas tem o primeiro nome

nome = input('Digite seu nome completo: ')
print(nome[1:6], nome[7:] )
print(nome[0], nome[6])
nome_sem_espaco = nome.replace(" ", "")
len(nome_sem_espaco)
print(len(nome_sem_espaco))
print(len(nome[:5]))



