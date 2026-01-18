'''
Ter uma função para ler a temperatura atual (simulada pelo usuário).

Ter uma função para decidir o estado do aquecedor:

Se temperatura < temperatura alvo → aquecedor LIGADO

Caso contrário → aquecedor DESLIGADO

Ter uma função para exibir o status do sistema.

Ter uma função principal que orquestra o sistema.
'''
temp_alvo = float(input('Digite a temperatura alvo: '))

def ler_temperatura():
    temp_atual = float(input('Digite a temperatura atual: '))
    return temp_atual

def controlar_aquecedor(temp_atual, temp_alvo):
    if temp_atual >= temp_alvo:
        return 'Aquecedor ligado'
    else:
        return 'Aquecedor desligado'

def status(temp_atual, temp_alvo, estado):
    print(f'Temperatura alvo: {temp_alvo} ºC')
    print(f'Temperatura atual: {temp_atual} ºC')

def main():
    temp_atual = ler_temperatura()
    estado = controlar_aquecedor(temp_atual, temp_alvo)
    status(temp_atual, temp_alvo, estado)

main()