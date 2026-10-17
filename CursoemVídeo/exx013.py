salario = float(input('Digite o seu salário: '))

aumento = salario * 15 / 100
valor = salario + aumento

print('')

print('Seu antigo salário era R$ {:.2f}'.format(salario))
print('Seu aumento foi R$ {:.2f}'.format(aumento))
print('Seu novo salário é R$ {:.2f}'.format(valor))
