def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n = 0):
    return n * 2


def triplo(n = 0):
    return n * 3


def metade(n = 0):
    return n / 2


def porc(n = 0):
    p  = n * 0.10
    return p + n

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')