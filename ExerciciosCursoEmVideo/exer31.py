
print('-'*41)
print(' Olá!Seja bem vindo ao aeroporto do João ')
print('-'*41)

viag = float(input('Quantos quilometros de distancia está a sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(viag))


if viag<=200:
    pre = viag * 0.50
    print('A sua viagem vai custar um total de R${}'.format(pre))
else:
    pre2 = viag * 0.45
    print('A sua viagem vai custar um total de R${}'.format(pre2))

