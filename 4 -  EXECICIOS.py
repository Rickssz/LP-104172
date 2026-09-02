import os
os.system("cls || clear")

codigo = input('Digite a matricula: ')
data = int(input('digite data de nascimento: '))
trabalho = int(input('Digite o tempo de trabalho: '))

idade = 2026 - data

print(f'\nMatricula: {codigo}')
print(f'Sua idade é: {idade} anos')
print(f'Tempo de contribuição: {trabalho} anos\n')

if idade >= 65 or trabalho >= 30:
    print('Você esta aposentado')
else:
    print('Você não está aposentado')