import os
os.system('cls')

soma = 0

while True:
    for i in range(2):
        nota = float(input('Digite a nota do aluno: '))
        if nota < 0 or nota > 10:
            print('Nota invalida! tente novamente.')
        else:
            soma += nota
            media = soma / 2

    print(f'Sua media é {media}')
    break
