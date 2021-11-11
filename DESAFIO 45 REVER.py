from random import choice
from time import sleep
print('========= Jokenpô =========')
print('O PC está escolhendo uma mão...')
mao = ['pedra','papel','tesoura']
esc = choice(mao)
print('PC já escolheu a mão, agora é a sua vez de escolher...')
p1 = str(input('Escolhe uma mão: Pedra, Papel ou Tesoura? '))
p1 = p1.strip().lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if p1 == esc:
    print('O PC escolheu {} e você escolheu {}'.format(esc,p1))
    print('Jogo empatado')
elif (p1 == 'pedra' and esc == 'tesoura') or (p1 == 'papel' and esc == 'pedra') or (p1 == 'tesoura' and esc == 'papel'):
    print('O PC escolheu {} e você escolheu {}'.format(esc, p1))
    print('Você venceu')
elif (esc == 'pedra' and p1 == 'tesoura') or (esc == 'papel' and p1 == 'pedra') or (esc == 'tesoura' and p1 == 'papel'):
    print('O PC escolheu {} e você escolheu {}'.format(esc, p1))
    print('O PC venceu')
else:
    print('Problemas tecnicos. Por favor, tente novamente;')