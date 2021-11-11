ano = int(input('Informe um ano: '))
print('O ano {} é BISSEXTO'.format(ano) if ano%4==0 and ano%400==0 else 'O ano {} NÃO É BISSEXTO'.format(ano))