def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n = 0, formato = False):
    res = n * 2
    return res if not formato else moeda(res)


def triplo(n = 0):
    return n * 3


def metade(n = 0, formato = False):
    res = n / 2
    return res if not formato else moeda(res)


def porc(n = 0, formato = False):
    res = n + (n * 0.10)
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')