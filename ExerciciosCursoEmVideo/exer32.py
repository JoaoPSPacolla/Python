import datetime

ano = int(input('Escreva um ano qualquer. Caso voce queira o ano atual, aperte 0:'))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é bissexto'.format(ano))
else:
    print('Esse ano {} não é bissexto'.format(ano))
