from time import sleep
print('>>> \033[31mMENU DE OPCOES\033[m <<<')
print('-=-' * 10)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
maior = 0
resposta = ''
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opcao = int(input('>>>> Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('---' * 10)
        print('\033[34mA soma entre {} + {} = {}\033[m'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('---' * 10)
        print('\033[34mO resultado de  {} x {} = {}\033[m'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            resposta = 'maior'
        elif n2 > n1:
            maior = n2
            resposta = 'maior'
        else:
            maior = n1 = n2
            resposta = 'iguais'
        print('---' * 10)
        print('\033[34mEntre os números {} e {}, o número {} é(são) {}\033[m'.format(n1, n2, maior, resposta))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('-=-' * 10)
        print('\033[36mFinalizando...\033[m')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('\033[33mFim do programa! Volte sempre!\033[m')



