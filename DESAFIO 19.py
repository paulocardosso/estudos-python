from random import choice
n1 = input('Informe o nome do aluno: ')
n2 = input('Informe o nome do aluno: ')
n3 = input('Informe o nome do aluno: ')
n4 = input('Informe o nome do aluno: ')
alunos = [n1,n2,n3,n4]
esc = choice(alunos)
#choice escolhe alguem da lista e retorna o valor escolhido
print('O aluno escolhido foi: {}'.format(esc))