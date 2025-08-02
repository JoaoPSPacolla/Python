import random

# A str, que vem antes de input, não é necessario

alun1 = str(input('Qual o primeiro aluno?'))
alun2 = str(input('Qual o noe do segundo aluno?'))
alun3 = str(input('Qual o nome do terceiro aluno?'))
alun4 = str(input('Qual o nome do quarto aluno?'))

alunos = (alun1, alun2, alun3, alun4)

print('O aluno escolhido foi {}'.format(random.choice(alunos)))


# O comando random.choice(alunos) significa que o
# programa vai escolher alguem aleatorio do conjunto ''alunos''
