numero = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in numero:
        numero.append(valor)#SE O VALOR NÃO ESTIVER EM 'NUMERO', O COMANDO ADICIONA ELE
                            #ELE TAMBÉM DESCORSIDERA OS VALORES QUE JÁ FORAM DIGITADOS,
                            #POIS ELE VAI PEGAR APENAS OS NUMEROS QUE NÃO ESTÃO EM'NUMERO',
                            #SE O NÚMERO JÁ FOI DIGITADO ANTES ELE JÁ ESTARÁ EM 'NUMERO', E POR ISSO NÃO SERÁ ADICIONADO DE NOVO
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
numero.sort()
print(f'Você digitou os valores {numero}')
