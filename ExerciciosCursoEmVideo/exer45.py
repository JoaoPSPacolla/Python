

REFAZER          REFAZER
REFAZER          REFAZER
REFAZER
REFAZER

from random import randint

itens = ('pedra' , 'papel' , 'tesoura')
computador = randint(0, 2)


print('Escolha uma das opções a baixo:')
print('[ 0 ] pedra')
print('[ 1 ] tesoura')
print('[ 2 ] papel')
jogador = int(input('Escolha sua opção: '))

numeros = ('pedra == 0', 'tesoura == 1', 'papel == 2')

print('='*25)
print('Você jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('='*25)

if computador == 0:
    if jogador == 0:
        print('Vocês empataram. Ambos jogaram pedra')
    elif jogador == 1:
        print('Que pena! Você perdeu')
    elif jogador == 2:
        print('Parabéns! Você ganhou')
elif computador == 1:
    if jogador == 0:
        print('Parabéns! Você ganhou')
    elif jogador == 1:
        print('Vocês empataram. Ambos jogaram tesoura')
    elif jogador == 2:
        print('Que pena! Você perdeu')
elif computador == 2:
    if jogador == 0:
        print('Que pena! Você perdeu')
    elif jogador == 1:
        print('Parabéns! Você ganhou')
    elif jogador == 2:
        print('Vocês empataram. Ambos jogaram papel')
