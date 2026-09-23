import os
os.system('cls')

for i in range(5):
    numeros = int(input(f'\nDigite o numero {i+1}: '))
    if numeros % 2 == 0:
        print(f'o numero {i} é par')
    else:
        print(f'O numero {i} é impar')