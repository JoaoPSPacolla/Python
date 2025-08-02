cont = soma = media = maior = menor = 0

resp = 's'

while resp == 's':
    num = float(input('Digite um número: '))
    resp = str(input('Quer continuar [s/n] ')).lower().strip() [0]
    cont += 1
    soma += num

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / cont

print('Você digitou {} números e a média entre eles é {:.2f}'.format(cont, media))
print('O maior valor foi {:.0f} e menor foi {:.0f}'.format(maior, menor))
print('ACABOU')
