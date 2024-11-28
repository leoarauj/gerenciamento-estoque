from services.estoque_service import cadastrar_estoque

nome = ""
categoria = ""
quantidade = 0

label_nome_produto = "Nome do Produto"
label_categoria_produto = "Categoria"
label_quantidade_produto = "Quantidade"
label_preco_produto = "Preço"
label_localizacao = "Localização"

def tratar_campo(campo, descricao):
    if isinstance(campo, (int, float, complex)):
        if not campo:
            print(f"O campo '{descricao}' está vazio, por favor preencha!")
            try: 
                #campo = int(input(f"- {descricao}: "))
                return int(input(f"- {descricao}: "))
            except ValueError:
                print("Operação cancelada!")
                return True

    elif not campo or len(campo) == 0:
        print(f"O campo '{descricao}' está vazio, por favor preencha!")
        campo = input(f"- {descricao}2: ")
        print(f"Valor Campo: {campo}")

        if len(campo) == 0:
            print("Operação cancelada!")
            return
        else:
            return campo

def formata_label(label):
    return f"- {label}: "

def main():
    estoque = {}

    while True:
        print("\n###### Gerenciamento de Estoque #####")
        print(" * 1. Cadastrar Produto")
        print(" * 0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input(formata_label(label_nome_produto))
            if not nome:
                nome = tratar_campo(nome, label_nome_produto)
                

            print(f"nome:: {nome}")


            categoria = input(formata_label(label_categoria_produto))
            if tratar_campo(categoria, label_categoria_produto):
                break
            print(f"categoria:: {categoria}")



            try:
                quantidade = int(input(formata_label(label_quantidade_produto)))
            except ValueError:
                 quantidade = 0
                 print("Entrada inválida! Por favor, digite um número inteiro.")

            if tratar_campo(quantidade, label_quantidade_produto): 
                break


            try:
                preco = float(input(formata_label(label_preco_produto)))
            except ValueError:
                preco = 0
                print("Entrada inválida! Por favor, digite um número inteiro ou decial.")

            if tratar_campo(preco, label_preco_produto):
                break


            localizacao = input(formata_label(label_localizacao))
            if tratar_campo(localizacao, label_localizacao): 
                break

            cadastrar_estoque(estoque, nome, categoria, quantidade, preco, localizacao)

        elif opcao == "0":
            print("Saindo do sistema!")
            break
        else:
            print("Essa opção não existe, por favor tente novamente!")

if __name__ == "__main__":
    main()
