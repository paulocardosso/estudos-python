from datetime import date
date = date.today().year
#import datetime
#date = int(datetime.datetime.now().date().strftime("%Y"))

anonasc = int(input('Informe o ano de nascimento: '))
idade = date - anonasc
if (idade<=9):
    print('MIRIM')
elif (idade<=14):
    print('INFANTIL')
elif (idade <= 19):
    print('JUNIOR')
elif (idade <= 20):
    print('SÊNIOR')
elif (idade > 20):
    print('MASTER')
else:
    print('Comando invalido')