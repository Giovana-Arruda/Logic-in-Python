def volumeFeijoada():
     while True:
         try:
            ml = float(input('Entre com a quantidade desejada(ml): '))
            if (ml >= 300) and (ml <= 5000):
                return ml * 0.08
            else:
                print('Não aceitamos porções menores que 300 ml ou maiores que 5l.')
                continue
         except ValueError:
             print('Você digitou um valor não numérico, tente novamente!')
             continue

def opcaoFeijoada():
    while True:
        print('Opções Disponíveis''\n'
              'B - Básica (Feijão + Paiol + Costelinha)\n'
              'P - Premium (Feijão + Paiol + Costelinha + Partes do Porco)\n'
              'S - Suprema (Feijão + Paiol + Costelinha + Partes do Porco + Charque + Calabresa + Bacon)\n')
        opcao = input('Qual é a opção escolhida?  ').upper()
        if opcao == 'B':
            return 1.00
        elif opcao == 'P':
            return 1.25
        elif opcao == 'S':
            return 1.50
        else:
            print('Opção inválida.')
            continue

def acompanhamentoFeijoada():
    subtotal = 0
    while True:
        try:
            print('MENU DE ACOMPANHAMENTOS\n'
                  '0 - Não desejo mais acompanhamentos (encerrar pedido)\n'
                  '1 - 200g de arroz \n'
                  '2 - 150g de farofa especial \n'
                  '3 - 100g de couve cozida \n'
                  '4 - uma laranja descascada')
            acomp = int((input('Deseja algum acompanhamento?  \n')))

            if acomp == 1:
                subtotal += 5
            elif acomp == 2:
                subtotal += 6
            elif acomp == 3:
                subtotal +=7
            elif acomp == 4:
                subtotal += 3
            elif acomp == 0:
                return subtotal
            else:
                print('Opção inválida.')

        except ValueError:
            print('Digite apenas os números disponíveis no menu.')
            continue

                        #começo do programa
print('Seja Bem-vindo(a) ao programa de Feijoada da Giovana.')
opcao = opcaoFeijoada()
ml = volumeFeijoada()
acomp = acompanhamentoFeijoada()
total = ml * opcao + acomp
print('O valor a ser pago é de R$ {:.2f}'.format(total))

