from uteis import numeros
preco = float(input('Digite o preço: R$ '))
print(f'A metade de R${preco} é R${numeros.metade(preco)}')
print(f'O dobro de R${preco} é R${numeros.dobro(preco)}')
print(f'Aumentando 10% temos R${numeros.porc(preco)}')