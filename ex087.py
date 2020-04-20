matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    coluna += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {coluna}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número valor da segunda linha é {maior}')

