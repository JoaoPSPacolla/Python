n1 = int(input('Qual o primeiro valor:'))
n2 = int(input('Qual o segundo valor:'))
n3 = int(input('Qual o terceiro valor:'))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))
