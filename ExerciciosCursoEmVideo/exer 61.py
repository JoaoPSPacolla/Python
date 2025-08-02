print('Gerador de PA')
print('-='*7)

print('Bem Vindo! Este é um gerador de PA, digite o primeiro valor e a razão para começarmos\nOBSERVAÇÃO: Digite apenas números inteiros ')


n = int(input('Primeiro valor:'))
raz = int(input('Razão da PA:'))

t = n
cont = 1

while cont < 11:
    print(t, end=' ')
    t = t + raz
    cont += 1


