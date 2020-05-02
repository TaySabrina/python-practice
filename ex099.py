from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('\033[34mAnalisando os valores passados...\033[m')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Programa Principal
maior(4, 7 , 2, 1, 5)
maior(3, 2, 5)
maior(8, 4)
maior(6)
maior()