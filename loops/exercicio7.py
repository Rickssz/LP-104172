import os
os.system('cls')

soma = 0
notas = 0
nota_limite = 2

while notas < nota_limite:
    nota = float(input('Digite sua nota:'))
        
    if nota < 0 or nota > 10:
        print('Nota invalida.')
        print('Tente novamente.')
        continue
    
    soma += nota
    notas += 1

media = soma / nota_limite
print(f'\nA média das notas é: {media:.2f}')
        