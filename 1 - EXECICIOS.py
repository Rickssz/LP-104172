import os
os.system ('cls || clear')

print('o preço das maças são R$ 1,30, mas caso compre 12 fica R$ 1.00')
maca = int(input('Digite quantas maçãs você quer: '))

if maca >= 12:
    valor_da_maca = 1.00
else:
    valor_da_maca = 1.30

valor_total = maca * valor_da_maca

print(f'A quantidade de maçãs foi: {maca}')
print(f'Valor total das maçãs foi: R$ {valor_total:.2f}')