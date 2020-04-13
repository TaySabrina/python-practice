print('{:=^40}'.format(' LOJAS SABRINA '))
preco = int(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[1] à vista em dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito''')
opcao = int(input('Opção escolhida: '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.')
print('Sua compra de R${:.2f} vai custar R${} no final'.format(preco, total))
