import os
os.system('cls || clear')

print('= SOLICITANDO DADOS =')
print()
n1 = int(input('Digite a seu número: '))
n2 = int(input('Digite seu número: '))
n3 = int(input('Digite seu número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
meio = (n1 + n2 + n3) - maior - menor

print('\n= EXIBINDO DADOS =')
print()
print(f'Os dois números são {n1}, {n2} e {n3}')
print(f'Maior número é: {maior}')
print(f'Menor número é: {menor}')
print(f'Menor número é: {meio}')