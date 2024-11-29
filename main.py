from services.estoque_service import cadastrar_estoque

label_nome_produto = "Nome do Produto"
label_categoria_produto = "Categoria"
label_quantidade_produto = "Quantidade"
label_preco_produto = "Preço"
label_localizacao = "Localização"

def verificar_campo_vazio(campo, descricao): 
    if isinstance(campo, (int, float, complex)):
        if not campo:
            print(f"O campo '{descricao}' está vazio, por favor preencha!")
            return True

    elif not campo or len(campo) == 0:
        print(f"O campo '{descricao}' está vazio, por favor preencha!")
        return True
    else:
        return False

def formata_label(label):
    return f"- {label}: "

def main():
    estoque = {}

    while True:
        print("\n###### Gerenciamento de Estoque #####")
        print(" * 1. Cadastrar Produto")
        print(" * 0. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                nome = input(formata_label(label_nome_produto))
                if verificar_campo_vazio(nome, label_nome_produto):
                    nome = input(formata_label(label_nome_produto))
                    if not nome:
                        print("Operação cancelada!")
                        continue
                
                categoria = input(formata_label(label_categoria_produto))
                if verificar_campo_vazio(categoria, label_categoria_produto):
                    categoria = input(formata_label(label_categoria_produto))
                    if not categoria:
                        print("Operação cancelada!")
                        continue

                quantidade = input(formata_label(label_quantidade_produto))
                if verificar_campo_vazio(quantidade, label_quantidade_produto):
                    quantidade = input(formata_label(label_quantidade_produto))
                    if not quantidade or quantidade == 0:
                        print("Operação cancelada!")
                        continue

                preco = input(formata_label(label_preco_produto))
                if verificar_campo_vazio(preco, label_preco_produto):
                    preco = input(formata_label(label_preco_produto))
                    if not preco or preco == 0:
                        print("Operação cancelada!")
                        continue

                localizacao = input(formata_label(label_localizacao))
                if verificar_campo_vazio(localizacao, label_localizacao):
                    localizacao = input(formata_label(label_localizacao))
                    if not localizacao:
                        print("Operação cancelada!")
                        continue

                cadastrar_estoque(estoque, nome, categoria, quantidade, preco, localizacao)
            case '0':
                print("Saindo do sistema!")
                break
            case _:
                print("Essa opção não existe, por favor tente novamente!")

if __name__ == "__main__":
    main()
