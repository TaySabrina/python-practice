from datetime import date
print('-=-' * 10)
print('ALISTAMENTO MILITAR...')
print(('-=-' * 10))
nasc = int(input('Ano de nascimento: '))
print('''Qual é o seu sexo?
[1] feminino
[2] masculino''')
sexo = int(input('Sua opcao: '))
atual = date.today().year
idade = atual - nasc


if idade == 18 and sexo == 2:
    print('Você tem que se alistar IMEDIATAMENTE!')
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
elif idade < 18 and sexo == 2:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
elif idade > 18 and sexo == 2:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
elif sexo == 1:
    print('Você é mulher, não precisa fazer alistamento militar obrigatório! ')


