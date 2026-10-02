import os
os.system('cls')

while True:
    print('--- MENU DE COMPRAS --- ')
    print('''    1. MACARRÃO || R$ 10.00
    2. ARROZ || R$ 5.00
    3. FEIJÃO || R$ 6.00
    4. FARINHA || R$ 7.00
    5. MONSTER || R$ 8.00
    ''')

    opcao = float(input('Digite o numero do item que quer: '))

    match opcao:
        case 1:
            item = 'MACARRÃO'
            valor = 10.00
            break
        case 2:
            item = 'ARROZ'
            valor = 5.00
            break
        case 3:
            item = 'FEIJÃO'
            valor = 6.00
            break
        case 4:
            item = 'FARINHA'
            valor = 7.00
            break
        case 5:
            item = 'MONSTER'
            valor = 8.00
            break

print('\n--- ITEM ESCOLHIDO E O PREÇO ---')
print(f'Item: {item}')
print(f'Valor: {valor}')