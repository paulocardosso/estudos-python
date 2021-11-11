from random import shuffle
n1 = str(input('Informe o nome do aluno: '))
n2 = str(input('Informe o nome do aluno: '))
n3 = str(input('Informe o nome do aluno: '))
n4 = str(input('Informe o nome do aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista) #embaralha a lista e não retorna nada, apenas uma ação sem retorno
print('A ordem de apresentação é: 1º {}; 2º {}; 3º {}; 4º {}.'.format(lista[0],lista[1],lista[2],lista[3]))