from math import sin,cos,tan,radians
a = int(input('Digite o ângulo: '))
print('O ângulo {:.2f} têm seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}'.format(a,sin(radians(a)),cos(radians(a)),tan(radians(a))))
