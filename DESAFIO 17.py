from math import pow,sqrt,hypot
co = float(input('Digite o comprimento do cateto oposto (cm): '))
ca = float(input('Digite o comprimento do cateto adjacente (cm): '))
h =  sqrt((pow(co,2))+(pow(ca,2)))
#h = hypot(co,ca)
print('O triângulo retangulo cujo cateto oposto {}cm e cateto adjacente {}cm, possui uma hipotenusa de {:.2f}cm'.format(co,ca,h))
