def luz(hora):
    if hora >= 0 and hora < 6:
        return 'apagada'
    if hora >= 6 and hora < 18:
        return 'meia-luz'
    if hora >= 18 and hora <= 24:
        return 'acesa'
    

hora = int(input('Digite a hora do dia: '))
luminosidade = luz(hora)
print(luminosidade)