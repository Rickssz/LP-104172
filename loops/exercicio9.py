import os
os.system('cls')

nota = 0
soma = 0

print('--- SOLICITANDO NOTAS ---')
for i in range(3):
    notas = float(input(f'Digite a sua {i+1} nota: '))
    if notas < 0 or notas > 10:
        continue
    soma += notas
    nota += 1
media = soma / 3

if media >= 7:
    resultado = 'Aluno aprovado'
elif media >= 5:
    resultado = 'Aluno esta de recuperação'
else:
    resultado = 'Aluno esta reprovado'

print('--- RESULTADO DE NOTAS ---')
print(f'media: {media}')
print(f'Situação do aluno: {resultado}')