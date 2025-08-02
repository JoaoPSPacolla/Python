
num = int(input('Digite um número [999 para parar]: '))
soma = cont = 0

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('FIM! A soma dos números digitados é {} e o total de digitado foi {}'.format(soma,cont))
