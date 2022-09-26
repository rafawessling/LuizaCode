nome1 = (input('Primeiro aluno: '))
nota1 = int(input(f'Nota {nome1}: '))

nome2 = (input('Segundo aluno: '))
nota2 = int(input(f'Nota {nome2}: '))

nome3 = (input('Terceiro aluno: '))
nota3 = int(input(f'Nota {nome3}: '))

nome4 = (input('Quarto aluno: '))
nota4 = int(input(f'Nota {nome4}: '))

lista = [nota1, nota2, nota3, nota4]

print(f'A maior nota foi: {max(numero for numero in lista)}')

# Outra forma de encontrar o maior valor:
# maior = max(lista)
# print(maior)
