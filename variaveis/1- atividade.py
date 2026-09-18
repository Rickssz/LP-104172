import os
os.system('cls || clear')

print('= SOLICITANDO DADOS =')
print()
primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

# Cálculos
soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print('\n= EXIBINDO RESULTADOS =')
print()
print(f'Média: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')