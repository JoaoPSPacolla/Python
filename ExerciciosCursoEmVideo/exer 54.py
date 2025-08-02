from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for c in range (1,8):
    nasc = int(input('Em qual ano nasceu a pessoa número {}:'.format(c)))
    idade = atual - nasc

    if nasc >= 18:
        totmaior += 1
    else:
        totmenor += 1

print('No total houveram {} pessoas maiores de idade \nE {} menores'.format(totmaior, totmenor))

