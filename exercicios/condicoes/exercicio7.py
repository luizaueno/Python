#  leia o salário do funcionário e calcule o valor do seu aumento. para salários superiores a 1250 10% e inferiores 15%

sal = int(input('Digite o valor do seu salário: '))

if(sal < 1250):
    aumento = sal + sal *(0.15)
    print('Parabéns! Seu novo salário é R$ {}'.format(aumento))
else:
    aumento = sal + sal * (0.1)
    print('Parabéns seu novo salário é R$ {}'.format(aumento))