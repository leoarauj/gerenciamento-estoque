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

def atualizar_estoque(estoque, nome, quantidade, tipo):
    if nome in estoque:
        if tipo == "entrada":
            estoque[nome]["quantidade"] += int(quantidade)
        elif tipo == "saida" and estoque[nome]["quantidade"] >= quantidade:
            estoque[nome]["quantidade"] -= quantidade
        else:
            print(f"\nErro: quantidade insuficiente para o produto '{nome}'.")
            return
        print(f"Estoque do produto '{nome}' atualizado com sucesso! Total: {estoque[nome]["quantidade"]}")
    else:
        print(f"Produto '{nome}' não encontrado.")