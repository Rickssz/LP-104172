import os
os.system('cls')

print('= SOLICITANDO DADOS =')
print()
valor = int(input('digite seu valor: '))

antecessor = valor - 1
sucessor = valor + 1

print('\n= EXIBINDO DADOS =')
print('seu valor é: ', valor)
print('seu antecessor é: ', antecessor)
print('seu sucessor é: ', sucessor)