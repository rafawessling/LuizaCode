# 6. Observe o seguinte programa. Escreva o que será impresso na tela caso o mesmo seja 
# executado com as seguintes entradas (5, 3).

try:
    number_1 = float(input('Insira um número: '))
    number_2 = float(input('Insira outro número: '))
    result = number_1 / number_2
    
    print('Resultado: {:.2f}'.format(resultado))
except ValueError:
    print('Isso não é um número.')
except ZeroDivisionError:
    print('Divisão por 0 indeterminada.')
except:
    print('Algo deu errado.')

# Resposta: Será impresso: 'Algo deu errado.', pois na hora de printar o resultado não foi 
# chamada a variável correta. Ou seja, temos variáveis não definidas. Mas essa exception 
# não se enquadra em ValueError e nem ZeroDivisionError, por isso cai na última exceção.
