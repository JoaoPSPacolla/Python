
palavras = ('REBELDE', 'SECADOR',
            'DINHEIRO', 'AZUL',
            'SABONETE', 'DOUTOR',
            'XERIFE', 'AMANHA',
            'HELICOPTERO', 'BANANA')

for c in palavras:
        print(f'\nA palavra {c} tem as vogais: ', end='')
        for letra in c:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')

