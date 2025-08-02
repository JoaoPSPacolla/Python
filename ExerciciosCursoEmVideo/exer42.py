c1 = float(input('Primeiro segmento:'))
c2 = float(input('Segundo segmento:'))
c3 = float(input('Terceiro segmento:'))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Os segmentos podem formar um triângulo', end='')
    if c1 == c2 == c3:
        print(' equilátero')
    elif c1 == c2 or c1 == c3 or c2 == c3:
        print(' isósceles')
    elif c1 != c2 != c3:
        print(' escaleno')
else:
    print('Não pode formar um triângulo')