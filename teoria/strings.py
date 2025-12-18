'''
uma cadeia de caractere que a gente conhece como frase chama Strings

Fatiamento: pedaços de Strings
exemplo: nome_variavel[9] 
apenas aquele caractere
exemplo: nome_variavel[9:13] 
pega até o caractere 12, um a menos

Analise
len(nome_da_variavel) - tamanho 
nome_da_variavel.count('o') - quantas vezes existe o o
nome_da_variavel.find('deo') - mostra onde começou
exemplo: 'curso ' in frase - retorna true

Transformação
nome_da_variavel.replace('Python', 'Android') - troca e sem nada tira os espaços do meio
nome_da_variavel.upper() - transforma em maiuscula, .lower() - minuscula
nome_da_variavel.capitalize() - deixa tudo minusculo e só a 1 maiuscula
nome_da_variavel.title() - quantas palavras tem, e colocar maiuscula na 1 de cada 
nome_da_variavel.strip() - tira os espaços extras da esquerda e direita
nome_da_variavel.rstrip() - tira da direita
nome_da_variavel.lstrip() - tira da esquerda

Divisão
nome_da_variavel.split()

Junção
'-'.join(nome_da_variavel)
print("""hello, esse exemplo é para imprimir textos longos""")
'''

frase = 'Curso em Vídeo Python'
print(frase[::2])