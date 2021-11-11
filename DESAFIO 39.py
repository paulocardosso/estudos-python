#import datetime
#date = int(datetime.datetime.now().date().strftime("%Y"))
from datetime import date

date = date.today().year

anonasc = int(input('Informe o ano de nascimento: '))
idade = date - anonasc
if (idade<18):
    falta = 18 - idade
    print('Você ainda falta {} anos para se alistar'.format(falta))
elif idade == 18:
    print('Esse é ano do seu alistamento')
elif idade > 18:
    passou = idade - 18
    print('Você já passou {} anos para se alistar'.format(passou))
else:
    print('Comando invalido')