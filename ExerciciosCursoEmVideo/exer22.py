nome = str(input('Digite seu nome')).strip()

print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#Na linha 1, o comando .strip serve para eliminar os espaços da esquerda e da direita

#Na linha 5 o comando len(nome) conta quantas letras tem, porém ele também conta os espaços
#Para eliminar os espaços, use o comando -(sinal de menos aqui) NOME.COUNT(' ')

#Na linha 6, para saber quantas letras tem o primeiro nome usa-se o comando, nome.find(' ')
#O programa lê todas as letras antes do primeiro espaço
