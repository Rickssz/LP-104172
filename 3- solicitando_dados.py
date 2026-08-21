import os
os.system("cls")

nome = input('Digite seu nome: ')
sobrenome = input('Digete seu sobrenome: ')
idade = int(input('Digete sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
nome_completo = (nome + sobrenome)

print()
print('nome: ', nome)
print('sobrenome: ', sobrenome)
print('idade:', idade)
print('peso: ', peso)
print('altura: ', altura)
print('NOME COMPLETO ', nome_completo)