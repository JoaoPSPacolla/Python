num = int(input('Digite um numero inteiro: '))
print('Escolha uma das opções para conversão')

print('[1] Converter para binario')
print('[2] Converter para octal')
print('[3] Converter para hexadecimal')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print('{} em binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} em octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Essa opção não é valida')

#O [2:] no if e nos elifs estão ali para o programa mostrar
# apenas o numero e nã a indicação do que é