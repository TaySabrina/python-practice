print('===' * 10)
print('{:^30}'.format('BANCO CEV'))
print('===' * 10)
valor = float(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totalced = 0
        if total == 0:
            break
print('===' * 10)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
