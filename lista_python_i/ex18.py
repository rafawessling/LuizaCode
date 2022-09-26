nota = int(input('Digite sua nota: '))

if nota >= 0 and nota <= 100:
  if nota >= 60:
    print(f'Nota: {nota}. Aprovado')
  else:
    print(f'Nota: {nota}. Reprovado')
else:
  print('Sua nota deve ser um valor entre 0 e 100')