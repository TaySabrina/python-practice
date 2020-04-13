from datetime import datetime
atual = datetime.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))