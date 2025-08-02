somaidade = 0
media = 0
maiorih = 0
nomevelho = ''

for c in range (1, 5):
    print('---- Pessoa número {} ----'.format(c))
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]:')).strip()

    somaidade = somaidade + idade

    if c == 1 and sexo in 'mM':
        maiorih = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maiorih:
        maiorih = idade
        nomevelho = nome

media = somaidade / 4
print('A media de idade é {}'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(maiorih, nomevelho))