'''
funcoes = rotina, algo que faz sempre                                        
'''      
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
  
                     
def contador(*num):
  tam = len(num)
  print(f'Recebi {tam} valores e são {num}')


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(list):
   pos = 0
   while pos < len(list):
      list[pos] *=2
      pos +=1       


# Programa principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)