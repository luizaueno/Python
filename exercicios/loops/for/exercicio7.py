# Faça um programa que percorra uma lista de umidade contendo os valores [30, 55, 20, 45, 25, 60]. Para cada valor abaixo de 40, imprima "Ligando Irrigação". Ao final, o programa deve exibir a quantidade total de vezes que a irrigação foi ligada.

umidade = [30, 55, 20, 45, 25, 60]
cont = 0
for i, valor in enumerate(umidade):
    if valor < 40:
        cont += 1
        print('Sensor {}: Ligando irrigação (Umidade: {}%)' .format(i, valor))
            
print('A irrigação foi ligada {} vezes '.format(cont))