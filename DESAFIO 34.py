salario = float(input('Informe o salario: '))
if salario > 1250.00:
    novsalario = salario * 1.10
else:
    novsalario = salario * 1.15
print('Seu aumento salarial é de R${:.2f}'.format(novsalario-salario))