import datetime

ano = int(input('Digite o ano em que você nasceu:'))


atual = datetime.date.today().year
idade = (atual - ano)

print('Você possui {} anos'.format(idade))

if idade<=9:
    print(' Categoria MIRIN ')
elif 14 >= idade >9:
    print(' Categoria INFANTIL ')
elif 19 >= idade >14:
    print(' Categoria JÚNIOR ')
elif 25 >= idade >19:
    print(' Categoria SÊNIOR ')
else:
    print(' Categoria MASTER ')