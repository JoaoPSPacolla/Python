co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vale {:.2f}' .format(h))


import math
co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
hi = math.hypot(co, ca)
print('A hopotenusa é igual a {:.2f}'.format(hi))

#Ambas as formulas estao certas