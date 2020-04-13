dias = int(input('Quantos dias o carro foi alugado? '))
quilometro = float(input('Quantos km foram percorridos pelo carro? '))
aluguel = dias * 60
percurso = quilometro * 0.15
soma = aluguel + percurso
print('O valor a pagar  do carro por {} dias e {}km alugados, será de R$ {:.2f}. '.format(dias, quilometro, soma))
