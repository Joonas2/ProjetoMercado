from menu import *
class Mercado:

    def __init__(self, nome, cnpj, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone


    def cadastro_funcionarios(self, nome, fone, salario):
        try:
            abre = open('funcionarios.txt', 'at+')
        except:
            pass
        else:
            self.nome = nome
            self.fone = fone
            self.salario = salario
            abre.write(f'{nome} {fone} {salario}\n')
        finally:
            abre.close()


    def cadastrar_clientes(self, nome, cpf, telefone):
        try:
            abre = open('cadastro_clientes.txt', 'at+')
        except:
            pass
        else:
            self.nome = nome
            self.cpf = cpf
            self.telefone = telefone
            abre.write(f'{nome} {cpf} {telefone}\n')
        finally:
            abre.close()

    def ver_funcionarios(self):
        try:
            abre = open('funcionarios.txt', 'rt+')
            ver_fucionarios_list = [funcinarios.split() for funcinarios in abre]
        except:
            pass
        else:
            grafico('Funcionarios')
            print('NOME     | CPF     | SALARIO')
            for funcarios in ver_fucionarios_list:
                print(f'{funcarios[0]} | {funcarios[1]} | {funcarios[2]}')


    def ver_cadastro_clientes(self):
        try:
            abre = open('cadastro_clientes.txt', 'rt+')
            ver_clientes_list = [clientes.split() for clientes in abre]
        except:
            pass
        else:
            grafico('Clientes ')
            print('Nome    | CPF | TELEFONE')
            for cliente in ver_clientes_list:
                print(f'{cliente[0]} | {cliente[1]} | {cliente[2]}')
        finally:
            abre.close()

#----------------------------------------------------------------------------------------------------------------------
    def cadastrar_produtos(self, produto,  quantidade, valor_und):
        try:
            abre = open('produtos.txt', 'at+')
        except:
            pass
        else:
            self.produto = produto
            self.quantidade = float(quantidade)
            self.valor_und = float(valor_und)
            self.valor_total = float(quantidade * valor_und)
            abre.write(f'{produto} {quantidade} {valor_und} {self.valor_total} \n')
        finally:
            abre.close()


    def venda_produto(self, nome_produto, valor_und, quantidade_vendida):
        try:
            abre = open('vendas.txt', 'at+')
        except:
            pass
        else:
            self.nome_produto = nome_produto
            self.valor_und = valor_und
            self.quantidade_vendida = -quantidade_vendida
            valor_total = quantidade_vendida * valor_und
            venda = self._atualizar_estoque(self.nome_produto, self.quantidade_vendida)

            if venda:
                abre.writelines(f'{nome_produto} {quantidade_vendida} {valor_und} {valor_total}\n')
            else:
                print('Produto não localizado')
        finally:
            abre.close()

    def _atualizar_estoque(self, nome_produto, quantidade):
        try:
            self.nome_produto = nome_produto
            self.quantidade_estoque = quantidade

            abre = open('produtos.txt', 'rt+')
            self.lista = [produto.split() for produto in abre]
            lista_produtos = self._transforma_float(self.lista)
            abre.close()

        except:
            pass
        else:
            #apos o for e o if, se o produto estiver na lista, vai abrir o arquivo e limpar ele 'wt', e depois será adicionado todos os valores
            # da list_produtos atualizados conforme a venda realizada
            procura_produto = self._localizar_produto(self.nome_produto, self.lista)

            if procura_produto:
                abre = open('produtos.txt', 'wt+')

                for pos, produtos in enumerate(lista_produtos):
                    if nome_produto == produtos[0]:
                        produtos[1] += self.quantidade_estoque
                        produtos[3] = produtos[1] * produtos[2]
                    abre.writelines(f'{produtos[0]} {produtos[1]} {produtos[2]} {produtos[3]}\n')
                return True
            else:
                return False
        finally:
            abre.close()


    def ver_estoque(self):
        try:
            abre = open('produtos.txt', 'rt+')
            ver_estoque_list =[produtos.split() for produtos in abre]
        except:
            pass
        else:
            print('PRODUTO | QUANTIDADE | VALOR UND | VALOR TOTAL')
            for produtos in ver_estoque_list:
                print(f'{produtos[0]} | {produtos[1]} | {produtos[2]} | {produtos[3]}')
        finally:
            abre.close()


    def _localizar_produto(self, nome_produto, lista):
        self.nome_produto_localizar = nome_produto
        self.lista_do_produto = lista

        for produtos in self.lista_do_produto:
            if self.nome_produto_localizar == produtos[0]:
                return True
            else:
                continue

    def _transforma_float(self, lista):
        self.lista = lista
        for pos, produtos in enumerate(lista):
            for ind, item in enumerate(produtos):
                if ind > 0:
                    item = float(item)
                    produtos[ind] = item
        return lista
