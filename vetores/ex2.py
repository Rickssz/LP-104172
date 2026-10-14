import os
os.system('cls')

livros = []

print('--- Solicitando nome dos livros ---')
for i in range(5):
    livros_nomes = input(f'Digite o nome do {i+1}º livro: ')
    livros.append(livros_nomes)
os.system('cls')

print('\n--- Nome dos livros ---')
for posicao, nome in enumerate(livros, start=1):
    print(f'{posicao}º livro: {nome}')