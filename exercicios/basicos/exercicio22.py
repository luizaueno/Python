# Leia um número de 0 a 9999 e mostre digitos separados
numero = int(input('Digite um número de 0 a 9999: '))
unidade = (numero // 1) % 10 
dezena = (numero // 10) % 10 
centena = (numero // 100) % 10 
milhar = (numero // 1000) % 10 
print('O número informado possui {} unidades, {} dezenas, {} centenas, {} milhares'.format(unidade, dezena, centena, milhar))