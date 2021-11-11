nome = str(input('Digite seu nome completo: ')).upper()
ver = 'SILVA' in nome
if ver:
    print('Sim, tem o nome SILVA ')
else:
    print('Não, não tem o nome SILVA')

'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
'''