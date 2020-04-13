tot18 = 0
tothomem = 0
totmulher = 0
print('---' * 10)
print('CADASTRE UMA PESSOA')
print('---' * 10)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]  ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tothomem} homens cadastrados.')
print(f'E temos {totmulher} mulheres com menos de 20 anos.')


