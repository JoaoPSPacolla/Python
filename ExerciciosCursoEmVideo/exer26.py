frase = str(input('Digite uma frase:')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a'.lower())))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))





# O mais 1 na linha 3, serve para o programa somar mais um na conta dele
# A primeira letra/numero/qualquer coisa sempre começar no zero
# Para que ele começasse a contar a partir do um colocou-se o +1