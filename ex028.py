from random import randint
from time import sleep
escolhido = randint(0, 5) #computador irá sortear um número
print('-=-' *20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' *20)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if num == escolhido:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(escolhido, num))
