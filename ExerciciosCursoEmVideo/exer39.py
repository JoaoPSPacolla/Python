from datetime import date

atual = date.today().year

anos = int(input('Em qual ano você nasceu? '))

idade = atual - anos

print('Você nasceu em {}, portanto sua idade é {} em {}'.format(anos, idade, atual ))

if idade == 18:
    print('Você deve se alistar nesse ano')
elif idade<18:
    falta = 18 - idade
    print('Aind faltam {} anos para o seu alistamento'.format(falta))
elif idade>18:
    passou = idade - 18
    print('O seu alistamento já foi a {} anos'.format(passou))
