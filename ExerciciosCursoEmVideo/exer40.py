n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))

media = (n1 + n2) / 2

if media >= 5 and media < 7:
    print('Sua media foi {:.1f}. Você está de RECUPERAÇÃO'.format(media))
elif media < 5:
    print('Sua media foi {:.1f}. Você está REPROVADO'.format(media))
else:
    print('Sua media foi {:.1f}. Você está APROVADO'.format(media))