

s = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]

while s not in 'MFmf':
    s = str(input('Dados inválidos. Por favor, informe seu sexo:')).upper().strip()[0]

print('Sexo {} registrado com sucesso'.format(s))


