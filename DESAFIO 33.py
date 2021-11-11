n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            menor = n3
        else:
            menor = n2
    else:
        maior = n3
        menor = n2
else:
    if n2 > n3:
        maior = n2
        if n1 > n3:
            menor = n3
        else:
            menor = n1
    else:
        maior = n3
        menor = n1
print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))