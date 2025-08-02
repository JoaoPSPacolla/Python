print('Gerador de PA')
print('-='*7)

print('Bem Vindo! Este é um gerador de PA, digite o primeiro valor e a razão para começarmos\nOBSERVAÇÃO: Digite apenas números inteiros ')


n = int(input('Primeiro valor:'))
raz = int(input('Razão da PA:'))

t = n
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(t, end=' ')
        print('-> ',end='')
        t = t + raz
        cont += 1

    print('Pausa')

    mais = int(input('Quantos termos vc quer mostrar a mais?'))

print('FIM')

print('O total de termos mostrados foi {}'.format(total))