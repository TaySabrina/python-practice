print('-=-' * 10)
print('{} MEDIA DE NOTAS {}'.format('\033[1;33m', '\033[m'))
print('-=-' * 10)
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Você foi {} REPROVADO.{}'.format('\033[31m', '\033[m'))
elif media == 5 and media <= 6.9:
    print('Você está de {}RECUPERAÇÃO.{}'.format('\033[33m', '\033[m'))
else:
    print('Você foi {}APROVADO!{}'.format('\033[34m', '\033[m'))
