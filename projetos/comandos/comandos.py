'''
sistema de comandos envolvendo módulos e manipulação de string. simulando a interpretação de um microcontrolador. ligado, desligado e status

'''

import datetime

status_inicial = 'desligado'
status_atual = 'ligado' or 'desligado'
comando = (input('(Ligar/Desligar) ')).upper().strip()
if(comando == 'LIGAR'):
    status_atual = 'ligado'
else:
    status_atual == 'desligado'
agora = datetime.datetime.now()
hora = agora.strftime("%H:%M:%S")
print('Ar condicionado {} às {} ' .format(status_atual, hora))


if(status_atual == 'ligado'):
    resposta = str(input('Seu ar condicionado está ligado. Deseja desligar? ')).lower()
    
    if(resposta == 'sim'):
        status_atual = 'desligado'
        print('Ar condicionado {} às {} ' .format(status_atual, hora))
    elif(resposta == 'nao'):
        status_atual ='ligado'
        print('Seu ar condicionado continua ligado ')
    else:
        print('Digite em minúsculo ')