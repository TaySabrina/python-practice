salario = float(input('Qual é o salário do funcionário? R$ '))
porc = salario * 0.15
aumento = salario + porc
print('Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario, aumento))
