cidade = input('Digite um nome de uma cidade: ')
div = cidade.split()
if div[0].upper() == 'SANTO':
    print('Sim, começa com o nome SANTO')
else:
    print('Não começa com o nome SANTO')
'''
cidade = str(input('Digite um nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
'''