valor_inicial = float(input('Valor inicial da parcela: '))
percentual = (float(input('Taxa de juros mensais (em %): '))) / 100
total_parcelas = int(input('Quantidade de parcelas: '))

valor_anterior = valor_inicial
parcela = 1

while parcela <= total_parcelas:
    valor_parcela = valor_anterior + (valor_anterior * percentual)
    valor_anterior = valor_parcela
    print(f'Parcela {parcela} - R$ {valor_parcela}')
    parcela += 1