produto = float(input('Qual é  preço do produto? R$ '))
desconto = produto * 0.05
promocao = produto - desconto
print('O produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(produto, promocao))
