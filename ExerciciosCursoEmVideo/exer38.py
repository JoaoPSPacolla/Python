n1 = float(input('Digite o primiero número:'))
n2 = float(input('Digite o segundo número:'))

if n1>n2:
    print('O {} é o maior número\nE o {} é o menor'.format(n1, n2))
elif n2>n1:
    print('O {:.0f} é o maior número\nE o {:.0f} é o menor'.format(n2, n1))
else:
    print('Ambos os valores são iguais')