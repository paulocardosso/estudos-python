print('============NUMERO PRIMO============')
n1 = int(input('Informe um número: '))
c1 = 0
for c in range(1,n1+1):
    if(n1%c==0):
        c1 += 1
if(c1<=2):
    print('O numero {} é PRIMO'. format(n1))
else:
    print('O numero {} não é PRIMO'.format(n1))

