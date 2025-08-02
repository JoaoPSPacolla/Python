
valor = (int(input(f'Digite um valor para a posição 1: ')),
        int(input(f'Digite um valor para a posição 2: ')),
        int(input(f'Digite um valor para a posição 3: ')),
        int(input(f'Digite um valor para a posição 4: ')))

print(f'Você digitou os valores {valor}')

print(f'O maior valor digitado foi {max(valor)} na posição {valor.index(max(valor))+1} ')
print(f'O menor valor digitado foi {min(valor)} na posição {valor.index(min(valor))+1}')