peso = float(input('Informe o seu peso (em Kg): '))
altura = float(input('Informe a sua altura (em m): '))
imc = peso / (altura)**2
print('Seu IMC é de {:.1f}'.format(imc))
if (imc < 18.5):
    print('Abaixo do peso')
elif (imc<=25):
    print('Peso ideal')
elif (imc<=30):
    print('Acima do Peso')
elif (imc <=40):
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')
else:
    print('Comando invalido')