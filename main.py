from Mercado import *
from menu import *
from time import sleep

while True:
    grafico('Menu')
    menu_escolhas()
    opcoes = int(input('Escolha uma opção: '))
    mercado = Mercado('Mercado', '0123123456', 93743527)

    if opcoes == 1:
        grafico('Menu Cadastros')
        menu_cadastro()
        opcoes_cadastro = int(input('Escolha uma opção: '))

        if opcoes_cadastro == 1:
            grafico('Cadastro Funcionarios')
            nome = input('Nome: ')
            fone = input('Fone: ')
            salario = input('Saalario: ')
            mercado.cadastro_funcionarios(nome, fone, salario)
            grafico('Cadastrando...')
            sleep(1)

        else:
            grafico('Cadastrar Clientes')
            nome = input('Nome: ')
            cpf = input('CPF: ')
            telefone = input('Fone: ')
            mercado.cadastrar_clientes(nome, cpf, telefone)
            grafico('Cadastrando...')
            sleep(1)

    elif opcoes == 2:
        grafico('Ver Cadastros')
        ver_cadastro()
        opcoes_ver_cadastro = int(input('Escolha uma opção: '))

        if opcoes_ver_cadastro == 1:
            mercado.ver_funcionarios()
        elif opcoes_ver_cadastro == 2:
            mercado.ver_cadastro_clientes()

    elif opcoes == 3:
        grafico('Cadastrar Produtos')
        produto = input('Produto: ')
        quantidade = float(input('Quantidade: '))
        valor_und = float(input('Valor und: '))
        mercado.cadastrar_produtos(produto, quantidade, valor_und)

    elif opcoes == 4:
        grafico('Ver Estoque')
        mercado.ver_estoque()

    elif opcoes == 5:
        grafico('Realizar venda')
        nome_produto = input('Produto: ')
        valor_und = float(input('Valor und: '))
        quantidade = int(input('Quantidade: '))
        mercado.venda_produto(nome_produto, valor_und, quantidade)


    elif opcoes == 6:
        grafico('Saindo...')
        break
