print('-=-' * 10)
print('EMPRÉSTIMO BANCÁRIO')
print('-=-' * 10)
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do Comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}.'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print('Empréstimo \033[31mNEGADO!\033[m')