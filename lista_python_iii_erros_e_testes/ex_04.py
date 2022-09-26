# 4. Observe o seguinte programa. Tendo em mente que ao executá-lo a exceção NameError 
#    é gerada, reescreve o código de forma com que tal exceção seja tratada.

try: 
    number = int(input('Digite um número: '))
    print('O número digitado foi:', n)
except NameError:
    print('Erro: NameError. Alguma variável não está definida')