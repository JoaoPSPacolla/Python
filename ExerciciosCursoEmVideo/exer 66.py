n = s = cont = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print('A soma foi dos {} valores foi {}'.format(cont, s))
