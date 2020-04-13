soma = cont = media = maior = menor = 0
cond = 'S'
while cond in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cond = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))


