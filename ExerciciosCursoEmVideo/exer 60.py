num = int(input('Digite um número para calcular o seu fatorial:'))
c = num
f = 1

while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))


# ESSE EXERCICIO PODERIA SER FEITO DE UMA MANEIRA MAIS FACIL,
# IMPORTANDO O COMANDO FACTORIAL, QUE SERVA PARA CALCULAR O FATORIAL
# MAS AQUI FOI FEITO COM OS COMANDOS WHILE