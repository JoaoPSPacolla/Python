cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input(f'Digite um número etre 0 e 20: '))
    if 0 <= num <= 20:
        break

print(f'Você digitou o número {cont[num]}')
