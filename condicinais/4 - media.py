import os
os.system('cls')

print('= SOLICITANDO DADOS')
print()
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
media = (primeira_nota + segunda_nota ) /2

print('\n= EXIBINDO DADOS')
print()
print('Seu nome é: ', nome)
print('Sua idade é: ', idade)
print('Sua primeira nota é: ', primeira_nota)
print('Sua segunda nota é: ', segunda_nota)
print('Sua media nota é: ', media)

if media >= 6:
    print('ENTÃO: ALUNO APROVADO')
else:
    print('ENTÃO: ALUNO REPROVADO')
    