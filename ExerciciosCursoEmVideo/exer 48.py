soma = 0
cont = 0

for c in range (1, 501, 2):
   if c % 3 == 0:
       cont = cont + 1  # Um contador soma/multiplica/divide 1 valor
       soma = soma + c  # Um somador soma/multiplica/divide um valor
print('A soma de todos os {} valores é {}'.format(cont, soma))