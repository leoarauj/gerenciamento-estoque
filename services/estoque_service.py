def cadastrar_estoque(estoque, nome, categoria, quantidade, preco, localizacao):
    if nome in estoque:
        print(f"Produto '{nome}' já foi cadastrado.")
    else:
        estoque[nome] = {
            "categoria": categoria,
            "preco": preco,
            "localizacao": localizacao,
            "quantidade": quantidade
        }
        print(f"\n( Produto '{nome}' cadastrado com sucesso! )")