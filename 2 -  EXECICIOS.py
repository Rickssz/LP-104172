import os
os.system ('cls || clear')

peso = float(input('Digite o peso do aluno: '))
altura = float(input('Digite a altura do aluno: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f}. Você está no peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f}. Você está acima do peso.')
elif 30 <= imc < 35:
    print(f'Seu IMC é {imc:.2f}. Você está com Obesidade Grau I.')
elif 35 <= imc < 40:
    print(f'Seu IMC é {imc:.2f}. Você está com Obesidade Grau II.')
else:
    print(f'Seu IMC é {imc:.2f}. Você está com Obesidade Grau III.')