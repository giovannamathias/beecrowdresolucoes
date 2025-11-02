#1010 Cálculo Simples

peca1 = input().split()
peca2 = input().split() 

cod1 = int(peca1[0])
quant1 = int(peca1[1])
valor1 = float(peca1[2])

cod2 = int(peca2[0])
quant2 = int(peca2[1])
valor2 = float(peca2[2])

valor_peca1 = quant1 * valor1
valor_peca2 = quant2 * valor2
valor_total = valor_peca1 + valor_peca2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
