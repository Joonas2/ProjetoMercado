def venda_produto(nome_produto, valor_und, quantidade_vendida):
    try:
        abre = open('vendas.txt', 'at+')
    except:
        pass
    else:
        nome_produto = nome_produto
        valor_und = valor_und
        quantidade_vendida = quantidade_vendida
        valor_total = quantidade_vendida * valor_und
        venda = _atualizar_estoque(nome_produto, -quantidade_vendida)

        if venda:
            abre.writelines(f'{nome_produto} {quantidade_vendida} {valor_und} {valor_total}\n')
        else:
            print('Produto não localizado')
    finally:
        abre.close()


def _atualizar_estoque(nome_produto, quantidade):
    try:
        nome_produto = nome_produto
        quantidade = quantidade

        abre = open('produtos.txt', 'rt+')
        lista = [produto.split() for produto in abre]
        lista_produtos = _transforma_float(lista)
        abre.close()

    except:
        pass
    else:
        procura_produto = localizar_produto(nome_produto, lista)

        if procura_produto:
            abre = open('produtos.txt', 'wt+')

            for pos, produtos in enumerate(lista_produtos):
                if nome_produto == produtos[0]:
                    produtos[1] += quantidade
                    produtos[3] = produtos[1] * produtos[2]
                abre.writelines(f'{produtos[0]} {produtos[1]} {produtos[2]} {produtos[3]}\n')
            return True
        else:
            return False
#___________________________________________________________________________________________________________

    finally:
        abre.close()


def _transforma_float(lista):
    lista = lista
    for pos, produtos in enumerate(lista):
        for ind, item in enumerate(produtos):
            if ind > 0:
                item = float(item)
                produtos[ind] = item
    return lista


def localizar_produto(nome_produto, lista):
    nome_produto_localizar = nome_produto
    lista_do_produto = lista

    for produtos in lista_do_produto:
        if nome_produto_localizar == produtos[0]:
            return True
        else:
            continue



venda_produto('Massa', 3.00, 5)
