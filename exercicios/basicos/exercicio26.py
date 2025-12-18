# 
n = input('Digite algo: ').upper().strip()
print(f'A letra "A" aparece {n.count("A")} vezes.')
print(f'A primeira letra A apareceu na posição {n.find("A")+1}.')
print(f'A ultima letra A aparece na posição {n.rfind("A")+1}.')