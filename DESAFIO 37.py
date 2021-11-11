n1 = int(input('Informe um número inteiro: '))
op = int(input('Informe qual a base para conversão: \n 1-Binário \n 2-Octal \n 3-Hexadecimal'))
if(op == 1):
    resul = format(n1, "b")
    print('O número decimal {} em binário é {}'.format(n1,resul))
elif(op == 2):
    resul = format(n1, "o")
    print('O número decimal {} em octal é {}'.format(n1, resul))
elif(op == 3):
    resul = format(n1, "x")
    print('O número decimal {} em hexadecimal é {}'.format(n1, resul))
else:
    print('Comando invalido, por favor tente novamente')