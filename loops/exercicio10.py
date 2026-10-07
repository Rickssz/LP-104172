import os
os.system('cls')

notas = []

while True:
    nota = float(input(f'Digite a {len(notas) + 1}ª nota: '))
    notas.append(nota)
    
    resposta = input('Deseja adicionar outra nota? (S/N): ').strip().upper()
    if resposta != 'S':
        break

media = sum(notas) / len(notas)
print(f'\nTotal de notas inseridas: {len(notas)}')
print(f'Média das notas: {media:.2f}')