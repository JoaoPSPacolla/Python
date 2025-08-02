from random import randint
v = 1

print('=-'* 13)
print('Vamos jogar par ou ímpar')
print('=-'* 13)

while True:
    jogador = int(input('Digite um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]')).upper().strip()[0]
    pc = randint(0, 11)
    total = jogador + pc
    print(f'Você jogou {jogador} e o computador jogou {pc}. O total deu {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
        else:
            print('Você perdeu')
            break
        print('Vamos jogar novamente')

print(f'GAME OVER! Você venceu {v} vezes')
