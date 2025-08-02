dias = int(input('Quantos dias o você ficou com o carro?'))
km = float(input('Quanto quilometros você rodou com esse carro?'))
prdia = dias * 60
prkm = km * 0.15
print('O valor a pagar é R${}'.format(prdia+prkm))
