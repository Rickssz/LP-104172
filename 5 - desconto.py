import os
os.system('cls')

print('= SOLICITANDO DADOS =')
valor = float(input('Digite o valor: '))

desconto = valor * 0.10 
valor_com_desconto = valor - desconto

print('\n= SOLICITANDO DADOS =')
print('Valor com desconto de 10%: ', valor_com_desconto)