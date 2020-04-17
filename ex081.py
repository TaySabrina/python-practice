lista = []
i = 0
v = 5
while True:
    resp = ' '
    lista.append(int(input('Digite um valor: ')))
    i += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {i} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if v not in lista:
    print('O valor 5 não foi encontrado na lista.')
else:
    print('O valor 5 faz parte da lista.')
