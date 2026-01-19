# paramêtro, dentro de () é o nome que a função usa para representar o valor que ela vai receber.
def sensor(temp):
    if temp < 30:
        return 'normal'
    if temp >= 30 and temp < 40:
        return 'alerta'
    if temp >= 40:
        return 'crítica'
    

# programa principal
temp = int(input('Digite a temperatura: '))
resultado = sensor(temp)
print(resultado)