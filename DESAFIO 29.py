vel = float(input('Informe a velocidade: '))
if vel>80.0:
    print('Você foi multado')
    custo = 7*(vel-80)
    print('O valor total da multa é: R${:.2f}'.format(custo))