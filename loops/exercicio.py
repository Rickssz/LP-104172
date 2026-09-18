import os
os.system('cls')

print('---TABELA---')
numero = int(input('Digite o numero: '))

for i in range(1, 11):
    print(f'{numero} + {i} = {numero + i}')

print('\n---TABELA---')
numero = int(input('Digite o numero: '))

for i in range(1, 11):
    print(f'{numero} - {i} = {numero - i}')

print('\n---TABELA---')
numero = int(input('Digite o numero: '))

for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')

print('\n---TABELA---')
numero = int(input('Digite o numero: '))

for i in range(1, 11):
    print(f'{numero} / {i} = {numero / i}')

