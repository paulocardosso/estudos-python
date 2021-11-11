dis = float(input('Informe a distância (em Km): '))
if dis <= 200.0:
    custo = 0.5 * dis
else:
    custo = 0.45 * dis
print('O custo total é de R${:.2f}'.format(custo))