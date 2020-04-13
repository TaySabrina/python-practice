print('---' * 10)
print('LOJA SUPER BARATÃO')
print('---' * 10)
totcompras = mais = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    totcompras += preco
    if preco > 1000:
        mais += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('---' * 10)
print('FIM DO PROGRAMA')
print('---' * 10)
print(f'O total de compras foi R${totcompras}')
print(f'Temos {mais} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')