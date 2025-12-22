#  leia as duas notas de um aluno, mostre a mnédia e uma mensagem: abaixo de 5, reprovado; entre 5 e 6.9 recuperação e acima disso aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2

if(m < 5):
    print('Reprovado(a)!')
elif(m > 5 and m <= 6.9):
    print('Em recuperação ')
else:
    print('Parabéns! Aprovado(a)!!')