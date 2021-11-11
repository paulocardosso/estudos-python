preconormal = float(input('Informe o preço do produto: '))
print('1- À vista (dinheiro ou cheque)\n2- À vista (cartão)\n3- Parcelado em 2 vezes\n4- Parcelado em 3 ou mais vezes')
formadpgto = int(input('Informe a forma de pagamento de acordo o número: '))

if formadpgto == 3 :
    precoapagar = preconormal
    print('O valor total a pagar é {}'.format(precoapagar))
elif formadpgto == 1:
    desc = preconormal*0.1
    precoapagar = preconormal-desc
    print('O valor total a pagar é {}'.format(precoapagar))
elif formadpgto == 2:
    desc = preconormal*0.05
    precoapagar = preconormal - desc
    print('O valor total a pagar é {}'.format(precoapagar))
elif formadpgto == 4:
    precoapagar = preconormal*1.20
    print('O valor total a pagar é {}'.format(precoapagar))
else:
    print('Comando invalido. Por favor, tente novamente')