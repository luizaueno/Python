def media (n1, n2, n3= 0):
    if n3 != 0:
        return (n1 + n2 + n3)/3
    else:
        return (n1 + n2)/2
    

def main():
    n1 =float(input('Informe sua nota 1: '))
    n2 =float(input('Informe sua nota 2: '))
    resposta = input('Deseja informar a nota 3? [s/n] ')
    if resposta == 's':
        n3 = float(input('Informe sua nota 3: '))
        resultado2 = media(n1, n2, n3)
        print(f'A média é igual a {resultado2:.2f}')
    else:
       resultado1 = media(n1, n2)
       print(f'A média é igual a {resultado1:.2f}')


main()