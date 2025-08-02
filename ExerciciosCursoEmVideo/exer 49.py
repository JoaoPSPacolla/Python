'''n = int(input('Digite um numero para ver a sua tabuada:'))

for c in range (0, 11):
    print(c * n, end=' ')'''


n = int(input('Digite um numero para ver a sua tabuada:'))

for c in range(1,11):
    print('{} x {} = {}'.format(n, c, n * c))

    ## AMBOS OS PROGRAMAS FUNCIONAM. SÓ QUE O PRIMEIRO NÃ MOSTRA A CONTA INTEIRA
    ## SOMENTE O RESULTADO, MAS TAMBÉM FUNCIONA