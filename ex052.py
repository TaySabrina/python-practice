num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m')
        tot += 1
    else:
        print('\033[31m')
    print('{} ', end = ' '.format(i))
print('\n\033[mO número {} foi divisível {} vez(e)s'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
