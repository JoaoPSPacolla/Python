velo = int(input('Qual a velocidade do carro?'))

if velo<=80:
    print('Muito bem,continue assim')
else:
    print('Você está acima da velocidade, reduza até estar em pelo menos 80km/h')
    multa = (velo-80) * 7
    print('Você vai receber uma multa de R${}'.format(multa))
