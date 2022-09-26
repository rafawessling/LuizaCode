prefixo = int(input('Prefixo (4 dígitos): '))
sufixo1 = int(input('Primeiro sufixo (4 dígitos): '))
sufixo2 = int(input('Último sufixo (4 dígitos): '))

print(f'Seus números de telefone são:')

sufixo = sufixo1
while sufixo <= sufixo2:
  print(f'{prefixo}-''{:0>4}'.format(sufixo))
  sufixo += 1
