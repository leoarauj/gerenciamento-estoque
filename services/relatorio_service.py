def gerar_relatorios(estoque):
    estoque_baixo = {nome: p for nome, p in estoque.items() if p["quantidade"] < 10}
    excesso_estoque = {nome: p for nome, p in estoque.items() if p["quantidade"] > 100}

    print("----------------------------------")
    print("\nRelatório de Estoque:")
    print("Produtos com Estoque Baixo:")
    for nome, p in estoque_baixo.items():
        print(f"- {nome}: {p['quantidade']} unidades")
    
    print("\nProdutos com Excesso de Estoque:")
    for nome, p in excesso_estoque.items():
        print(f"- {nome}: {p['quantidade']} unidades")

    print("----------------------------------")