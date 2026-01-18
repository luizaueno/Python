def somar(a, b):
    resultado = a + b
    return resultado

def mostrar(resultado):
    print(resultado)

def main():
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    resultado = somar(a, b)
    mostrar(resultado)


main()