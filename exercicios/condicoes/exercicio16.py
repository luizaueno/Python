#  Calcule o IMC de uma pessoa: abaixo de 18.5 Abaixo do peso entre 18.5 e 25 peso ideal 25 a 30 sobrepeso; 30 a 40 obesidade; acima de 40 obesidade mórbida 

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura * altura)
if imc < 18.5:
     print('Você está abaixo do peso ')
elif imc == 18.5 <= 25:
     print('Você está no peso ideal ')
elif imc > 25 <= 30:
     print('Você está em sobrepeso ')
elif imc > 30 <= 40:
     print('Você está na obesidade ')
else:
     print('Você está na obesidade mórbida ')