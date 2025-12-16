''' 
+ adição; - subtração; 
* multiplicação; / divisão; 
** potencia; // divisão inteira; 
% resto da divisão 


5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5**2 == 25
5//2 == 2
5%2 == 1

== igual a 
= recebe
ordem: () ** */ // % + -

quebra linha /n 
não quebra linha, no fim colocar end=' '
'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, O produto vale {}, e a Divisão vale {:.2f}'.format(s, m, d))
print('A divisão inteira vale {}, e a exponenciação vale {}'.format(di, e))


