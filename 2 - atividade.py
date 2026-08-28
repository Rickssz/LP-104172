import os
os.system('cls || clear')

print('= SOLICITANDO DADOS =')
print()
idade = int(input('Digite a sua idade: '))

print('\n= EXIBINDO DADOS =')
print()
if idade < 16:
    print('Não pode votar.')

elif (idade >= 16 and idade <= 17) or idade >= 66:
    print('Voto opcional.')

else:
    print('Voto obrigatório.')