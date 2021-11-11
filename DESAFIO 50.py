print('============SOMA DE NUMEROS PARES DIGITADO PELO USUARIO============')
soma = 0
for c in range(0,6):
    n = int(input('Informe um numero: '))
    if (n % 2 == 0):
        soma = soma + n
print('O valor da soma apenas dos numeros pares é {}'.format(soma))
