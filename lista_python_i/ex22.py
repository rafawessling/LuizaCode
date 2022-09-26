num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
num4 = int(input('Quarto número: '))
num5 = int(input('Quinto número: '))

lista = [num1, num2, num3, num4, num5]

#Lista de valores de forma ordenada
lista.sort()
print(lista)

#A contagem de cada número
for numero in set(lista):
    ocorrencias = lista.count(numero)
    print(f'{numero}: {ocorrencias}x')

#Identificar se é par ou ímpar, e se é primo ou não 
pares = [x for x in lista if x % 2 == 0]
impares = [x for x in lista if x % 2 != 0]


for numero in set(pares):
  print(f'{numero}, par')

for numero in set(impares):
  print(f'{numero}, ímpar')

