num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''
forma com texto
if (len(num) == 4):
    print('Unidade: {}'.format(num[3]))
    print('Dezena: {}'.format(num[2]))
    print('Centena: {}'.format(num[1]))
    print('Milhar: {}'.format(num[0]))
if(len(num) == 3):
    print('Unidade: {}'.format(num[2]))
    print('Dezena: {}'.format(num[1]))
    print('Centena: {}'.format(num[0]))
if(len(num) == 2):
    print('Unidade: {}'.format(num[1]))
    print('Dezena: {}'.format(num[0]))
if(len(num) == 1):
    print('Unidade: {}'.format(num[0]))
'''
