valor_emprestimo = float(input('Valor do empréstimo: '))
taxa = float(input('Taxa de juros mensais (em decimais): '))
tempo = int(input('Meses para pagar: '))

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

print(f'O valor final que irá pagar ao banco é {valor_final}')