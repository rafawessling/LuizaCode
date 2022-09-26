# 2. Faça um programa que calcule a divisão de dois números m e n e trate os casos em
#    que n = 0.

try: 
    m = float(input('Numerador: '))
    n = float(input('Denominador: '))
    result = m / n
    print(f'Resultado: {result}')
except ZeroDivisionError:
    print("Não existe divisão por zero")
