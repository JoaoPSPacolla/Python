from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')

pc = randint(0,10)
palpites = 1

escolha = int(input('Qual a sua escolha?'))

while escolha != pc:
    if escolha < pc:
        print('Errou... O número que estou pensando é maior... Tente de novo')
        escolha = int(input('Qual a sua escolha?'))
        palpites += 1
    if escolha > pc:
        print('Errou... O número que estou pensando é menor... Tente de novo')
        escolha = int(input('Qual a sua escolha?'))
        palpites += 1

print('Parabéns! Você acertou em {} tentativas.'.format(palpites))



