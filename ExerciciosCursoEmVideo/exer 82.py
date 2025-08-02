lista = []
pares = list()
impares = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

lista.sort()
print(f'A lista original é {lista}')

for i, v in enumerate(lista):            # REVER AULA PARA ENTENDER ISSO
    if v % 2 == 0:                       # PROCURAR ENTENDER SOBRE O ENUMERATE E ESSE RESTO
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista dos pares é {pares}')
print(f'A lista dos impares é {impares}')
