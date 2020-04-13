soma = 0
cont = 0
for i in range(1, 7):
    n = int(input('Digite {}° número: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} números par(es) é {}'.format(cont, soma))
