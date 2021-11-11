r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if abs(r2 - r3) < r1 < r2 + r3 and abs(r1 - r3) < r2 < r1 + r3 and abs(r2 - r1) < r3 < r2 + r1:
    print('As três retas podem formar um triângulo.')
    if (r1 == r2 == r3):
        print('EQUILATERO')
    elif (r1 == r2 != r3) or (r2 == r3 != r1) or (r1 == r3 != r2):
        print('ISOSCELES')
    else:
        print('ESCALENO')
else:
    print('As três retas não podem formar um triângulo.')