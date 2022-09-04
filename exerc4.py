codigo = 0 #contador
listaProd = []

def cadastrarProduto(): #função de cadastramento
    prod = input('Digite o nome do produto:  ')
    fab = input('Digite o nome do fabricante:  ')
    valor = float(input('Digite o valor do produto:  '))
    cod = codigo + 1
    prod_dic = {'Código': codigo, 'Produto': prod, 'Fabricante': fab,}
    listaProd.append(prod_dic.copy()) #o .append acrescenta objetos no final da lista.

def consultarProduto():
    while True:
        try:
            opcao = int(input('Bem-vindo(a) ao menu de consulta de produtos:\n'
                  '1 - Consultar todos os produtos\n'
                  '2 - Consultar produto por código\n'
                  '3 - Consultar produto por fabricante\n'
                  '4 - Retornar\n'
                          ''))
            if opcao == 1:
                print('Consultar todos os produtos')
                for prod in listaProd:
                    for key, value in prod.items(): #key é a chave definida entre '' e o value é o valor acrescentado dentro dessa chave.
                        print('{} : {}'.format(key,value))
            elif opcao == 2:
                print('Consultar produto por código.')
                entradacod = int(input('Entre com o código desejado:  '))
                for prod in listaProd:
                    if prod['Código'] == entradacod:
                     for key, value in prod.items():
                        print('{} : {}.'.format(key,value))
            elif opcao == 3:
                print('Consultar produto por fabricante.')
                entradafab = input('Entre com o nome do fabricante: ')
                for prod in listaProd:
                    if prod['Fabricante'] == entradafab:
                     for key, value in prod.items():
                        print('{} : {}.'.format(key, value))
            elif opcao == 4:
                print('Retornar ao menu principal')
                break
            else:
                print('Opção inválida.') #opção numérica não disponível no menu.

        except ValueError: #se o usuário digitar um valor não numérico no input.
            print('Valor não inteiro.')

def removerProduto(): #função para remover o produto da lista através de seu código.
    print('Opção de remover produto escolhida.')
    entrada = int(input('Digite o código do produto:  '))
    for produto in listaProd:
        if(produto['codigo']) == entrada:
            listaProd.remove(produto) #.remove é uma type que remove itens de uma lista.


# COMEÇO DO PROGRAMA PRINCIPAL #
print('Bem-vindo(a) ao programa de cadastro de produtos da Giovana.') #apresentação inicial!
while True:#enquanto o usuário não utilizar a opção 4(sair) essas opções ficarão se repetindo.
    try:
        print('Digite a opção desejada\n'
                  '1 - Cadastrar produto\n'
                  '2 - Consultar produto\n'
                  '3 - Remover produto\n'
                  '4 - Sair\n'
                  '')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            codigo += 1 #contabiliza o código em um intervalo de +1.
            cadastrarProduto()
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Encerrando o programa...')
            break
        else: #se o usuário digitar um número não disponível no menu, cai aqui.
            print('Opção inválida. Digite apenas os números disponíveis no menu.')
    except ValueError: #se o usuário digitar um valor errado(não inteiro, como o input pede), cai no except.
        print('Opção inválida. Se atente aos números disponíveis no menu.')
