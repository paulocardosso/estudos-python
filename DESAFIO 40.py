n1 = float(input('Informe a nota da 1ª unidade: '))
n2 = float(input('Informe a nota da 2ª unidade: '))
m = (n1+n2)/2
if m >= 7:
    print('APROVADO')
elif m>=5:
    print('RECUPERAÇÃO')
elif m<5:
    print('REPROVADO')
else:
    print('Comando invalido')