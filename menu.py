def linha():
    print('-=' * 20)


def grafico(txt):
    linha()
    print(f'{txt.center(40)}')
    linha()

def menu_escolhas():
    menu = ['1) Cadastrar Funcionarios | Clientes', '2) Ver Cadastros Clientes| Funcionarios', '3) Cadastrar Produtos', '4) Ver Estoque', '5) Vendas', '6) Sair']
    for op in menu:
        print(op)

def menu_cadastro():
    menu_cad = ['1) Cadastrar Funcionarios', '2) Cadastrar Clientes']
    for op in menu_cad:
        print(op)

def ver_cadastro():
    menu_cad = ['1) Ver cadastro funcionarios', '2) Ver cadastro clientes']
    for op in menu_cad:
        print(op)


'''menu = ['1) Cadastrar Funcionarios', '2) Cadastrar Cliente', '3) Cadastrar Produtos', '4) Ver funcionarios', '5) Ver Cliente', '6) Ver Estoque', '7) Sair']'''