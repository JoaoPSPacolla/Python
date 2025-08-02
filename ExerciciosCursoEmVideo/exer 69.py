print('-' * 20)
print('Cadastre uma pessoa')
print('-' * 20)
mais18 = homens = mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    print('-' * 35)
    if mais18 >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer cadastar mais alguem? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
    print('-' * 35)

print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todos temos {homens} cadastrados')
print(f'E temos {mulheres20} de mulheres com menos de 20 anos')
