from services.estoque_service import cadastrar_estoque, atualizar_estoque, rastrear_localizacao
from services.relatorio_service import gerar_relatorios

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

def mockCadastro(estoque):
    cadastrar_estoque(estoque, "Produto A", "Categoria X1", 50, 10.0, "Prateleira 1")
    cadastrar_estoque(estoque, "Produto B", "Categoria X2", 110, 20.0, "Prateleira 2")
    cadastrar_estoque(estoque, "Produto C", "Categoria X3", 150, 30.0, "Prateleira 3")
    cadastrar_estoque(estoque, "Produto D", "Categoria X4", 9, 40.0, "Prateleira 4")
    cadastrar_estoque(estoque, "Produto E", "Categoria X5", 2, 50.0, "Prateleira 5")
    cadastrar_estoque(estoque, "Produto F", "Categoria X6", 5, 60.0, "Prateleira 6")

def main():
    estoque = {}

    mockCadastro(estoque)

    while True:
        print("----------------------------------")
        print("###### Gerenciamento de Estoque ######")
        print(" * 1. Cadastrar Produto")
        print(" * 2. Atualizar Estoque")
        print(" * 3. Rastrear Localização")
        print(" * 4. Gerar Relatórios")
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

                quantidade = int(input(formata_label(label_quantidade_produto)))
                if verificar_campo_vazio(quantidade, label_quantidade_produto):
                    quantidade = int(input(formata_label(label_quantidade_produto)))
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

            case '2':
                nome = input(formata_label(label_nome_produto))
                if nome in estoque:
                    tipo = input("Tipo de movimentação (entrada/saida): ").lower()
                    quantidade = int(input(formata_label(label_quantidade_produto)))
                    atualizar_estoque(estoque, nome, quantidade, tipo)
                else:
                    print("----------------------------------")
                    print(f"\nProduto '{nome}' não encontrado.")

            case '3':
                nome = input("Nome do Produto: ")
                localizacao = rastrear_localizacao(estoque, nome)
                if localizacao:
                    print("----------------------------------")
                    print(f"\nLocalização do produto '{nome}': {localizacao}")
                else:
                    print("----------------------------------")
                    print(f"\nProduto '{nome}' não encontrado.")
            case '4':
                gerar_relatorios(estoque)
            case '0':
                print("Saindo do sistema!")
                break
            case _:
                print("Essa opção não existe, por favor tente novamente!")

if __name__ == "__main__":
    main()
