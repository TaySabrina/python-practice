from time import sleep
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 25)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):  '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')