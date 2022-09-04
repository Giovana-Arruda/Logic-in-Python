ac = 0 #variável acumuladora.
print('Bem-vindo(a) à Pizzaria da Giovana.\n'
      '---------------------- Cardápio ----------------------\n'
      '| Código | Descrição  | Pizza Média | Pizza Grande   |\n'
      '|   21   | Napolitana | R$ 20,00    | R$ 26,00       |\n'
      '|   22   | Marguerita | R$ 22,00    | R$ 26,00       |\n'
      '|   23   | Calabresa  | R$ 25,00    | R$ 32,50       |\n'
      '|   24   | Toscana    | R$ 30,00    | R$ 39,00       |\n'
      '|   25   | Portuguesa | R$ 30,00    | R$ 39,00       |\n'
      '-----------------------------------------------------')

while True:
    tam = input('Qual o tamanho desejado? (M/G):  ').upper()
    if tam == 'M' or tam == 'G':
        cod = int(input('Digite o código do sabor desejado:  '))
    else:
        print('Opção inválida. Digite apenas M ou G!')
        continue #volta para o início do looping, na variável 'tam'.
    if cod == 21:
        sab = 'Napolitana'
        if tam == 'M':
            ac += 20
        else:
            ac += 26
    elif cod == 22:
            sab = 'Marguerita'
            if tam == 'M':
                ac += 22
            else:
                ac += 26
    elif cod == 23:
            sab = 'Calabresa'
            if tam == 'M':
                ac += 25
            else:
                ac += 32.50
    elif cod == 24:
            sab = 'Toscana'
            if tam == 'M':
                ac += 30
            else:
                ac += 39
    elif cod == 25:
            sab = 'Portuguesa'
            if tam == 'M':
                ac += 30
            else:
                ac += 39
    else:
        print('Opção de código inválida.')
        continue
    print('Você pediu uma pizza {} de sabor {}.'.format(tam, sab))
    cont = input('Deseja pedir algo mais?(S/N): ').upper()
    if cont == 'S':
        continue #volta para o início do programa.
    else:
        print('O valor total do seu pedido é de R${:.2f}'.format(ac))
        break # o programa é finalizado.
