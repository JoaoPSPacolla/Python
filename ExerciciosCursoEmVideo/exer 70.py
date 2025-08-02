print('=' * 18)
print('LOJA SUPER BARATÃO')
print('=' * 18)

cont1000 = total = cont = menor = 0
barato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        cont1000 += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('------- FIM DO PROGRAMA -------')
print(f'O total de compras foi R${total}')
print(f'Ao todo temos {cont1000} produtos que custam mais de R$1000')
print(f'O produto mais barato foi o {barato}, que custou R${menor}')

