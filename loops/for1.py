import os
os.system('cls')

numeros = []

for i in range(5):
    num = int(input(f'Digite os {i+1}°: '))
    numeros.append(num)
    
print(f'Seu numeros foram: {numeros}')
print(f'A soma de seus numeros é: {sum(numeros)}')
