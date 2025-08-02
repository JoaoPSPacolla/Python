print('=' * 10,'Lojas John', '=' * 10)

compra = int(input('Preço total das compras: R$'))
print('FORMAS DE PAGAMENTO ')

print('[ 1 ] À vista no dinheiro ou cheque (10% de desconto)')
print('[ 2 ] À vista no cartão (5% de desconto)')
print('[ 3 ] 2x no cartão (preço normal)')
print('[ 4 ] 3x ou mais no cartão (20% de juros)')

esc = int(input('Escolha a forma de pagamento: '))

if esc == 1:
    desc = (compra * 10 / 100)
    total = (compra - desc)
    print('A sua compra de {} vai sair por {} com o desconto de 10%'.format(compra, total))
elif esc == 2:
    desc = (compra * 5/100)
    total = (compra - desc)
    print('A sua compra de {} vai sair por {} com o desconto de 5%'.format(compra, total))
elif esc == 3:
    print('A sua compra fica {}'.format(compra))
elif esc == 4:
    aum = (compra * 20/100)
    total = (compra + aum)
    print('A sua compra de {} vai ficar {} com o aumento de 20%'.format(compra, total))
else:
    print('Opção invalida')
