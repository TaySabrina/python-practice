from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[31mPEDRA, PAPEL, TESOURA\033[m
\033[1mSuas opções:\033[m 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')
print('-=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=-' * 11)
if computador  == 0: #computador jogou pedra
    if jogador == 0:
        print('{}EMPATE!{}'.format('\033[36m', '\033[m'))
    elif jogador == 1:
        print('{}VOCÊ VENCEU!{}'.format('\033[33m', '\033[m'))
    elif jogador == 2:
        print('{}COMPUTADOR VENCEU!{}'.format('\033[34m', '\033[m'))
    else:
        print('{}JOGADA INVÁLIDA{}'.format('\033[31m', '\033[m'))

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('{}COMPUTADOR VENCEU!{}'.format('\033[34m', '\033[m'))
    elif jogador == 1:
        print('{}EMPATE!{}'.format('\033[36m', '\033[m'))
    elif jogador == 2:
        print('{}VOCÊ VENCEU!{}'.format('\033[33m', '\033[m'))
    else:
        print('{}JOGADA INVÁLIDA{}'.format('\033[31m', '\033[m'))

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('{}VOCÊ VENCEU!{}'.format('\033[33m', '\033[m'))
    elif jogador == 1:
        print('{}COMPUTADOR VENCEU!{}'.format('\033[34m', '\033[m'))
    elif jogador == 2:
        print('{}EMPATE!{}'.format('\033[36m', '\033[m'))
    else:
        print('{}JOGADA INVÁLIDA{}'.format('\033[31m', '\033[m'))
