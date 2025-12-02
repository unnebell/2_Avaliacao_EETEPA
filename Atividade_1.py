produtos = []
# Criação de while com except valueError para tratamento de dados errados

while True:
    try:
        qtd_produtos = int(input("Digite a quantidade de produtos que deseja adicionar: "))

        for i in range(qtd_produtos):
            nome_produto = input("Digite o produto: ")
            qtd_estoque = int(input("Digite a quantidade: \n"))

            produtos.append([nome_produto, qtd_estoque])

        i = 0

        while i < qtd_produtos:
            try:
                for produto in produtos:
                    i += 1
                    print(f"Produto {i}: {produto[0]} - Quantidade em estoque: {produto[1]}")

                    if produto[1] < 10:
                        print("ALERTA: Estoque baixo!\n")
                    else:
                        print("Estoque OK.\n")
            except ValueError:
                print("[ERRO] Entrada inválida! Tente novamente.\n")
            
    except ValueError:
        print("[ERRO] Entrada inválida! Tente novamente.\n")