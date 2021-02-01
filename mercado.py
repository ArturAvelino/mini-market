from time import sleep
from Models.produto import Produto
from utils.helper import formata_valor

produtos = []
carrinho = []


def main():
    menu()


def menu():
    print("================================================================")
    print("======================== Bem-vindo(a)! =========================")
    print("========================= Tuca's Shop ==========================")
    print("================================================================\n")
    print("Selecione uma opção abaixo: ")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Comprar Produto")
    print("4 - Visualizar Carrinho")
    print("5 - Fechar Pedido")
    print("6 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)
        exit()
    else:
        print("Opção inválida")
        sleep(2)
        menu()


def cadastrar_produto():
    print("Cadastro de produtos")
    print("====================")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    produto = Produto(nome, preco)
    p = None
    for each in produtos:
        if each.nome == nome:
            p = each.nome
    if p == produto.nome:
        print("O produto já está cadastrado")
        sleep(2)
        menu()
    else:
        produtos.append(produto)
        print(f"O produto {nome} foi cadastrado com sucesso!")
        sleep(2)
        menu()


def listar_produtos():
    if len(produtos) > 0:
        print("Listagem de produtos")
        print("====================")
        for produto in produtos:
            print(f"{produto} \n")
            sleep(1)
        menu()
    else:
        print("Não existe produtos cadastrados")
        sleep(2)
        menu()


def comprar_produto():
    if len(produtos) > 0:
        print("Informe o código do produto que deseja comprar")
        print("==============================================")
        print("============Produtos Disponíveis==============")
        print("==============================================")
        for n in produtos:
            print(f"{n}\n")
        codigo = int(input("Código: "))
        produto = pega_produto_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho = False
                for item in carrinho:
                    quant = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f"O {produto.nome} agora posssui {quant + 1} unidades")
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho")
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho!")
        else:
            print(f"O produto com o código {codigo} não foi encontrado")
        sleep(2)
        menu()
    else:
        print("Não existe produtos cadastrados")
    sleep(2)
    menu()


def visualizar_carrinho():
    if len(carrinho) > 0:
        print("Produtos do carrinho: ")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}\n")
                sleep(2)
                menu()
    else:
        print("Ainda não existem produtos no carrinhos")
        sleep(2)
        menu()


def fechar_pedido():
    if len(carrinho) > 0:
        valor_total = 0
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}\n")
                valor_total += dados[0].preco * dados[1]
                sleep(1)
        print(f"Sua fatura é: {formata_valor(valor_total)}")
        print("Volte sempre!")
        carrinho.clear()
        sleep(5)
    else:
        print("Não existe produtos no carrinho")
        sleep(2)
        menu()


def pega_produto_codigo(codigo):
    p = None
    for each in produtos:
        if each.codigo == codigo:
            p = each
    return p


if __name__ == "__main__":
    main()
