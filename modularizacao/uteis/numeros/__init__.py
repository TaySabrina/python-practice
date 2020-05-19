def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def triplo(n=0):
    return n * 3


def metade(n=0, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def porc(n=0, taxa=0, formato=False):
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)


def reducao(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5 ):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{porc(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{reducao(preco, taxar, True)}')