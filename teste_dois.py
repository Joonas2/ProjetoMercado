arquivo = open('produtos.txt', 'rt+')



def localizar_produto(nome_produto, lista):
    nome_produto_localizar = nome_produto
    lista_do_produto = lista

    for produtos in lista_do_produto:

        if nome_produto_localizar == produtos[0]:
            print(produtos, 'Deu')
            return True

        else:
            print(produtos, 'Não deu')
            continue

teste = 'Arroz'
lista_produtos = [produto.split() for produto in arquivo]
localizar_produto(teste, lista_produtos)