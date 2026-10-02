import os
os.system('cls')

login_correto = input('Digite seu usuario: ')
senha_correta = int(input('Digite sua senha: '))
os.system('cls')

while True:
    login = input('Digite o login: ')
    senha = int(input('Digite a senha: '))

    if login == login_correto and senha == senha_correta:
        print('Bem-vindo!')
        break
    else:
        print('''\nLogin ou senha inválidos.
tente novamente.
        ''')
    input('Pressione uma tecla pra continaur...')
    os.system('cls')