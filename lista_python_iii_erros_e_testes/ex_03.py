# 3. Observe o programa abaixo. Reescreva esse código de uma forma com que ele seja capaz de tratar a inserção
#    de um caractere por parte do usuário

try: 
    number = int(input('Digite um número: '))
    print('O número digitado foi:', number)
except ValueError:
    print('Erro no tipo de dado')