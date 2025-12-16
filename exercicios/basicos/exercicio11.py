#  leia a altura e largura em metros, calcule a area, e a quantidade de tinta(1 litro = 2m²)
a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
area = a * l
tinta = area // 2
print('A quantidade de tinta gasta para essa área é {} litros'.format(tinta))