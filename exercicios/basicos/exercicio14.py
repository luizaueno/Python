#14 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = int(input('Digite a temperatura em ºC: '))
tempF = (tempC * 1.8) + 32
print('A temperatura Celsius inserida em Fahrenheit é igual a: {:.2f}'.format(tempF))

