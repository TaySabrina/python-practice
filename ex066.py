i = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    i += 1
print(f'O resultado da soma dos número é {soma} e foram digitados {i} números.')