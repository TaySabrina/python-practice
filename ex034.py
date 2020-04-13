salario = float(input('Digite o seu salário: R$ '))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
print('Seu salário agora será no valor de R$ {}{}{}'.format('\033[33m', aumento, '\033[m'))