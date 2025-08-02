nome = str(input('Qual seu nome completo?')).strip()

print('O seu nome tem Silva? {}'.format('silva' in nome.lower()))



# O ''.lower()'' juntamente com as letras de ''silva'' todas minusclas faz com que o programa
# nao tenha aquele erro de dar como falso o nome só porque
# não está escrito com todas as letras em maiusculo ou minusculo
# Poderia também ser feito a função ''.upper'' no lugar de ''.lower''
# e junto do upper colocar todas as letras de ''Silva'' em maiusculas
