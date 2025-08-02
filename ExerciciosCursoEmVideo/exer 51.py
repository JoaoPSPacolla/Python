n1 = int(input('Primiero termo:'))
raz = int(input('Razão:'))
decimo = n1 + (11-1) * raz

for c in range (n1, decimo, raz):
    print(c, end= ' - ')

print('Assim por diante')