a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

print(f'{a}x² + {b}x + {c} = 0')

delta = (b ** 2) - 4 * a * c

if a == 0:
  print('O valor de a, deve ser diferente de 0')
elif delta < 0:
  print('Sem raízes reais')
else:
  x1 = (- b + delta ** (1 / 2)) / (2 * a)
  x2 = (- b - delta ** (1 / 2)) / (2 * a)

  print(f'As raízes dessa equacão são: x1 = {x1} e x2 = {x2}')