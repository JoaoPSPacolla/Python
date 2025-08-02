casa = float(input('Qual o valor da casa? R$'))
sala = float(input('Qual o salario do comprador? R$'))
anos = float(input('Quantos anos de financiamento?'))

prest = casa / (anos * 12)

print('Para pagar uma casa de R${} em {:.0f}, é preciso uma prestação de R$ {:.2f}'.format(casa, anos, prest))

if sala> 30 / 100:
    print('Emprestimo negado')
else:
    print('Emprestimo aceito')