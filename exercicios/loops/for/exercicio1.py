# Mostre na tela uma contagem regressiva e de uma pausa de 1 segundo entre cada um

import time
print('Contagem regressiva! ')
for contagem in range(10, 0, -1):
    print(contagem)
    time.sleep(1)

