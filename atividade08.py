# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;
valor = float(input("insira o valor da sua compra (R$)"))
desconto = float(input("insira o valor em (%) do desconto"))
desconto = desconto / 100
print('Valor com desconto: R$', valor * (1-desconto) )
