def desconto(preco):
    return preco - (0.1 * preco)

def mostrar(valor):
    print(valor)

def main():
    preco = float(input('Informe o valor do produto: '))
    valor = desconto(preco)
    mostrar(f'O valor do produto passa a ser: {valor}')


main()