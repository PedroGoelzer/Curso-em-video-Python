valor = float(input('Digite o valor do produto: '))

des = valor * 5 / 100
final = valor - des

print('O valor inicial era R$ {:.2f}'.format(valor))
print('O desconto foi de R$ {:.2f}'.format(des))
print('O valor final era R$ {:.2f}'.format(final))