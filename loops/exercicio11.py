import os
os.system('cls')

familias = []
salario = []
filhos_lista = []



while True:
    print('''--- MENU ---
1. Cadastrar Familias
2. Sair e exibir
''')
    
    opcao = int(input('Digite a opção que você quer: '))

    match opcao:
        case 1:
            familia = input('Digite a familia: ')
            salarios = float(input('Digite o salario da familia: '))
            filhos = int(input('Digite quantos filhos tem: '))

            familias.append(familia)
            salario.append(salarios)
            filhos_lista.append(filhos)

            print('\nFamília cadastrada com sucesso!')
            input('Pressione Enter para continuar...')
            
        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            total_familias = len(familias)

            # Verifica se alguma família foi cadastrada para evitar divisão por zero
            if total_familias > 0:
                media_salarial = sum(salario) / total_familias
                media_filhos = sum(filhos_lista) / total_familias
                maior_salario = max(salarios)
                menor_salario = min(salarios)

                print('--- RESULTADO FINAL ---')
                print(f'Total de famílias cadastradas: {total_familias}')
                print(f'Média salarial: R$ {media_salarial:.2f}')
                print(f'Média de filhos por família: {media_filhos:.1f}')
                print(f'Maior salário: R$ {maior_salario:.2f}')
                print(f'Menor salário: R$ {menor_salario:.2f}')
            else:
                print('Nenhuma família foi cadastrada.')

            break

        case _:
            print('Opção inválida!')
            input('Pressione Enter para tentar novamente...')