# 7. Uma colega tentou executar o seguinte programa. E obteve a seguinte mensagem de erro.
# Reescreva o código para que esse erro seja exibido de forma mais clara e amigável.

try:
    file = open('file.txt', 'r')
    file_lines = file.readline()
    file.close()
except FileNotFoundError:
    print('Esse arquivo não foi encontrado.')