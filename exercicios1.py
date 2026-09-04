import os
os.system('cls')

notas1 = float(input('Digite sua nota: '))
notas2 = float(input('Digite sua nota: '))
notas3 = float(input('Digite seu nota: '))
faltas = int(input('Digite suas faltas: '))

soma = notas1 + notas2 + notas3
media = soma / 3

if media >= 7 and faltas <=40:
    print('parabens aluno aprovado')
else:
    print('aluno reprovado')