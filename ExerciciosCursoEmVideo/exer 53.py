name = str(input('Digite uma frase:')).strip().upper()
palavras = name.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) - 1, -1, -1 ):
    inverso += junto[c]

if inverso == junto:
    print('O inverso de {} é {} \n Essa frase é um palindromo,ou seja, ela é igual de trás para frente e de frente para trás'.format(junto, inverso))
else:
    print('O inverso de {} é {} \n Essa frase não é um palindromo,ou seja, ela não é igual de trás para frente e de frente para trás'.format(junto, inverso))
