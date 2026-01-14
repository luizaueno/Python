# função escreva() que recebe um texto e mostre uma linha de acordo com o tamanho

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)



# programa principal
escreva('Luiza')
escreva('Programadora Python')