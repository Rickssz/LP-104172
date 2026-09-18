import os
os.system ('cls || clear')

produtos = ["Teclado", "Mouse", "Monitor"]
estoque = [10, 15, 5]

print(f"Os produtos que temos são: {produtos}")
print(f"O estoque disponível é: {estoque}\n")

while True:
    produtos_buscados = input('Digite o item que quer: ')
    if produtos_buscados.lower() == 'sair':
        print("Saindo do sistema...")
        break

    if produtos_buscados in produtos:
        posicao = produtos.index(produtos_buscados)

        if estoque[posicao] > 0:
            estoque[posicao] -= 1

            print(f'Sucessão voce comprou 1 {produtos_buscados}')
            print(f"Novo estoque de {produtos_buscados}: {estoque[posicao]}\n")
        else:
            print(f"Ops! {produtos_buscados} está esgotado.\n")
            
    else:
        print("Produto não encontrado no cadastro!\n")
