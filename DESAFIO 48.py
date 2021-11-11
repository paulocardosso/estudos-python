print('============SOMA DE NUMEROS IMPARES E MULTIPLO DE 3============')
soma = 0
for c in range(1,500+1,2):
    if (c%3 == 0):
        soma = soma + c
print('O valor da soma de todos os impares e multiplo de 3 é {}'.format(soma))