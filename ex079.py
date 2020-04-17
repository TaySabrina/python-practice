from time import sleep
lista = []
while True:
    resp = ' '
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        sleep(0.5)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar.')
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
lista.sort()
print(f'Você adicionou os valores {lista}')