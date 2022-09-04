print('Bem-vindo(a) à loja da Giovana!') #apresentação pessoal.
valor = float(input('Digite o valor do produto: R$  ')) #pergunta ao usuário o valor do produto.
quant = int(input('Digite a quantidade: ')) #pergunta ao usuário a quantidade.

if quant <= 4:  #Se a quantidade do produto for menor ou igual a 4: nenhum desconto será aplicado!
    valorfinal = valor * quant
    print('O valor é de R${}.' .format(valorfinal))

elif (quant >= 5) and (quant <= 19): #Se a quant do produto estiver entre 5 e 19,
    # o programa cai nessa condicional, aplicando desconto de 3% por unidade.
    valorfinal = valor * quant
    desconto = valorfinal - valorfinal * 0.03
    print('O valor sem desconto é de R${:.2f}' .format(valorfinal))
    print('O valor com desconto é de R${:.2f} (desconto de 3% aplicado!)' .format(desconto))

elif (quant >= 20) and (quant <= 99): #Se a quant do produto for entre 20 e 99 unidades, desconto de 6%.
    valorfinal = valor * quant
    desconto = valorfinal - valorfinal * 0.06
    print('O valor sem desconto é de R${:.2f}' .format(valorfinal))
    print('O valor com desconto é de R${:.2f} (desconto de 6% aplicado!)' .format(desconto))

else:   # Se o valor for maior que 100 unid, se aplica o desconto de 10%.
    valorfinal = valor * quant
    desconto = valorfinal - valorfinal * 0.10
    print('O valor sem desconto é de R${:.2f}' .format(valorfinal))
    print('O valor com desconto é de R${:.2f} (desconto de 10% aplicado!)' .format(desconto))

print('Obrigado por comprar conosco!')
