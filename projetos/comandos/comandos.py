'''
sistema de comandos envolvendo módulos e manipulação de string. simulando a interpretação de um microcontrolador. ligado, desligado e status

'''

import datetime

status_inicial = 'desligado'
comando = (input('Digite:(Ligar/Desligar) ')).upper().strip()
status_atual = comando
agora = datetime.datetime.now()
hora = agora.strftime("%H:%M:%S")
print('Ar condicionado {} às {} ' .format(status_atual, hora))