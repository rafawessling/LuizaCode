nome = input('Informe o seu nome: ')
cidade = input('Informe sua cidade de nascimento: ')
ano = input('Informe o seu ano de nascimento: ')

anos = 2030 - int(ano)

print(f'Olá {nome}')
print(f'Sua cidade de nascimento é {cidade}')
print(f'Você nasceu no ano {ano}')
print(f'Em 2030, você terá {anos} anos')