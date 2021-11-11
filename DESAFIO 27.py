nome = str(input('Digite o nome completo: '))
div = nome.split()
print('Primeiro Nome: {}'.format(div[0]))
print('Sobrenome: {}'.format(div[len(div)-1]))