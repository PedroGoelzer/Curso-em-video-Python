lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = lar * alt
tinta = area / 2

print('')
print('sua parede tem {:.2f} de largura'.format(lar))
print('')
print('sua parede tem {:.2f} de altura'.format(alt))
print('')
print('sua parede tem {:.2f} de área'.format(area))
print('')
print('Você precisará usar {:.2f} litros de tinta '.format(tinta))