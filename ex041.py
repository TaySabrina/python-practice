from datetime import date
print('-=-' * 10)
print('{}...CLASSIFICANDO ATLETAS...{}'.format('\033[1;33m', '\033[m'))
print('-=-' * 10)
nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('CATEGORIA: MIRIM')
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
elif idade <= 19:
    print('CATEGORIA: JUNIOR')
elif idade <= 25:
    print('CATEGORIA: SENIOR')
else:
    print('CATEGORIA: MASTER')
