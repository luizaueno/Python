'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre - os com idade em um dicionário
Se for diferente de 0, informe o ano de contratação e o salário. Diga com quantos anos a pessoa se aposenta 
''' 
nome = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = 2026
idade = ano_atual - ano_nascimento
carteira = int(input('Digite a carteira de trabalho ou 0 se não tiver: '))

if carteira != 0:
    ano_contratacao = int(input('Em que ano você foi contratado? '))
    idade_contratada = ano_contratacao - ano_nascimento
    idade_aposenta = (idade_contratada + 35)
    salario = float(input('Informe seu salário: '))
    print(f'Voce se aposenta aos {idade_aposenta} anos')
    funcionario = {'nome':nome, 'idade':idade, 'carteira':carteira, 'contratacao':ano_contratacao, 'salario':salario, 'aposentadoria':idade_aposenta}
    print(funcionario)
else:
    pessoa = {'nome':nome, 'idade':idade, 'carteira':carteira}
    print(pessoa)
   