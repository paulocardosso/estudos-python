valor = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salario mensal: '))
anos = float(input('Informe em quantos anos deseja pagar pelo imovel: '))

valormensal = (valor/anos)/12
valorposs = (30*salario)/100
if (valormensal > valorposs):
    print('O emprestimo foi negado')
    print('O valor mensal é de R${:.2f}/mês e excede 30% do seu salario mensal que conrresponde a R${:.2f}'.format(valormensal,valorposs))
else:
    print('O emprestimo foi aprovado')
    print('O valor mensal é de R${:.2f}/mês e não excede 30% do seu salario mensal que conrresponde a R${:.2f}'.format(valormensal,valorposs))