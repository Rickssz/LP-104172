import os
os.system('cls')

while True:
    numero = int(input('Digite um número: '))
    if numero < 1 or numero > 10:
        print('Numero invalido, tente novamente.')
    else:
        print('Numero esta entre 1 e 10')
        break