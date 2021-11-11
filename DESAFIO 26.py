frase = str(input('Digite uma frase: ')).strip().upper()
qa = frase.count('A')
print('A quantidade da letra A é: {}'.format(qa))
pp = frase.find('A')+1
print('A primeira letra A está na posição: {}'.format(pp))
pu = frase.rfind('A')+1
print('A última letra A está na posição: {}'.format(pu))