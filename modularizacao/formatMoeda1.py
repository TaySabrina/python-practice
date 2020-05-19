from uteis import numeros
p = float(input('Digite o preço: R$ '))
print(f'A metade de {numeros.moeda(p)} é {numeros.metade(p, True)}')
print(f'O dobro de {numeros.moeda(p)} é {numeros.dobro(p, True)}')
print(f'Aumentando 10% temos {numeros.porc(p, True)}')