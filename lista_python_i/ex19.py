venda = float(input('Valor da venda '))

if venda < 1000:
  print('Você não ganhará comissão desta venda')
elif venda >= 1000 and venda < 5000:
  comissao = venda * 0.1
  print('Você ganhará R${:.2f} de comissão'.format(comissao))
elif venda >= 5000 and venda < 10000:
  comissao = venda * 0.2
  print('Você ganhará R${:.2f} de comissão'.format(comissao))
elif venda >= 10000 and venda < 50000:
  comissao = venda * 0.25
  print('Você ganhará R${:.2f} de comissão'.format(comissao))
else:
  comissao = venda * 0.3
  print('Você ganhará R${:.2f} de comissão'.format(comissao))