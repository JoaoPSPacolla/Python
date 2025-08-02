print('-' * 40)
print('           Listagem de preços      ')
print('-' * 40)

produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Estojo', 5.20,
            'Lápis de cor', 2.10,
            'Apontador', 1.80,
            'Caderno', 15,
            'Lapiseira', 8.90)

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>6.2f}')