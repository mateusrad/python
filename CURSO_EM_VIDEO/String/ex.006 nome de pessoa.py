nome = input('Digite seu nome completo:').upper()
nome_separado = nome.split()
ultimo_nome = len(nome_separado)
print(f'O nome digitado foi \n{nome}')
print(f'O 1º nome é {nome_separado[0]}')
print(f'O ultimo nome é {nome_separado[-1]}')