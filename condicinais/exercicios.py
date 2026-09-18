import os
os.system('cls')

login = ('Richard').lower()
senha = (101107)

login1 = input('Digite seu login: ')
senha2 = int(input('Digite sua senha: '))

if login1 == login and senha2 == senha:
    print('Bem-vindo!')
else:
    print('login ou senha inválidos')