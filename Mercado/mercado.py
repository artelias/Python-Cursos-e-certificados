from typing import List, Dict
from time import sleep

from Models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==================================')
    print('========= Bem vindo(a) ===========')
    print('======= BEMAIS SUPERMERCADO=======')
    print('==================================')

    print('Selecione uma opcao abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produtos()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opcao invalida')
        menu()


def cadastrar_produtos() -> None:
    print('Cadastrar produto')
    print('=================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input(' Informe o preco do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('======')
            sleep(1)
            menu()

    else:
        print('Ainda ao existe esse produto cadastrado')
        sleep(2)
        menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo do produto desejado:')
        print('----------------------------------------')
        print('============Produto Disponiveis ==============')
        for produto in produtos:
            print(produto)
            print('--------------------------------------------')
            sleep(1)

        codigo: int = int(input())

        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicomado ao carrinho')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print('O produto com codigo {codigo} nao foi encontrado')
            sleep(2)
            menu()
    else:
        print('Ainda nao existe produto')
        sleep(2)
        menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f' Quantidade: {dados[1]}')
                print('--------------------------')
                sleep(1)
    else:
        print(' nao tem nada no carrinho')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('----------------------------------')
                sleep(1)
        print(f'Sua fatura eh {formata_float_str_moeda(valor_total)}')
        print('volte sempre')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda nao existe rodutos no carrinho')
    sleep(2)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
