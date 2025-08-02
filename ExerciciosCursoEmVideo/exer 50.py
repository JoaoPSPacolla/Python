soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números pares e a soma deles é {}'.format(cont, soma))
