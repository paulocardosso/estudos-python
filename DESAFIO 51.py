print('============PROGRESSÃO ARITIMETICA============')
a1 = int(input('Informe o primeiro termo (a1): '))
r = int(input('Informe a razão da PA: '))
cont = 0
for c in range(a1,10000+1,r):
    cont += 1
    if(cont<=10):
        print('O {}º termo é {}'.format(cont,c))
print('FIM')