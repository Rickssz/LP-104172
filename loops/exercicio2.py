import os
os.system('cls')

while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota < 0 or nota > 10:
        print('Nota invalida! tente novamente.')
    else:
        print(f'Sua nota é: {nota}')
        break