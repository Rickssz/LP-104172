import os
os.system('cls')

login_correto = "richard1"
senha_correta = 10220

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