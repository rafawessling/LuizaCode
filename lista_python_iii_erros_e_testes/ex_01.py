# 1. Faça um programa que calcule a raiz quadrada de um número n e trate os casos
#    em que n < 0. 
#    OBS: Utilize o módulo math para calcular a raiz quadrada.

import math
from typing import Type

def raiz_validate(num):
        if num <= 0:
            raise TypeError("O número deve ser maior que 0")

def raiz():
    try: 
        num = float(input('Número: '))
        raiz_validate(num)
    except TypeError as error:
        print(error)
        return
    
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')

raiz()