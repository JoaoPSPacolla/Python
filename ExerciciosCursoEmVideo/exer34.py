sala = float(input('Digite o seu salario:'))

if sala>1250:
    aumento = (sala * 10/100) + sala
    print('Você teve um aumento de 10% no seu salario. A partir de agora ele passará a ser {}'.format(aumento))
else:
    aumento = (sala * 15/100) + sala
    print('Você teve um aumento de 15% no seu salario. A partir de agora ele passará a ser {}'.format(aumento))