import random
print('O computador está pensando em um número entre 0 a 5')
nesc = random.randint(0,5)
print('O computador pensou no número')
nuser = int(input('Qual o número que o Computador pensou? (entre 0 a 5)'))
print('VENCEU. O número que o Computador pensou foi {}'.format(nesc) if nesc == nuser else 'PERDEU. O número que o Computador pensou foi {}'.format(nesc))