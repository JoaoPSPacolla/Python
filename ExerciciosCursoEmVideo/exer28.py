from random import randint
from time import sleep
pc = randint(0, 5)

print('Eu vou pensar em um numero entre 0 e 5, tente adivinhar')
n = int(input('Qual numero você acha que pensei?'))  #Quando coloquei str deu errado, com int foi certo
print('Carregando...')
sleep(2)

if n==pc:
    print('Parabéns, voce acertou')
else:
    print('KKKKK, voce errou. Eu pensei no numero {}'.format(pc))


#Essa função sleep faz com que o computador leve algum tempo para processar
#Para usa-lo é necessario usar o ''from time import sleep'' ou então ''import sleep''
