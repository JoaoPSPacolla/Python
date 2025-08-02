cont = 0
numero = list()

while True:
    valor = int(input('Digite um valor: '))
    cont += 1
    if valor not in numero:
        numero.append(valor)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Você digitou {cont} valores')     # EU USE O CONT, QUE FUNCIONOU, MAS TAMBÉM PODERIA TER USADO O LEN
numero.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numero}')

if 5 in numero:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')