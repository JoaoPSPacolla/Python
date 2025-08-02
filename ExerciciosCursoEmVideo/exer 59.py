n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))

opcao = 0

while opcao != 5:
    print('''             [ 1 ] SOMAR
             [ 2 ] MULTIPLICAR
             [ 3 ] MAIOR
             [ 4 ] NOVOS NÚMEROS
             [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual sua opção:'))

    if opcao == 1:
        soma = n1 + n2
        print('A soma dos dois números é {}'.format(soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação dos dois números é {}'.format(multiplica))
    elif opcao == 5:
        print('FIM')
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {}, o {} é maior'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {}, o {} é maior'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite um valor:'))
        n2 = int(input('Digite um valor:'))
    else:
        print('Opção invalida; Tente novamente')
    print('=' * 40)