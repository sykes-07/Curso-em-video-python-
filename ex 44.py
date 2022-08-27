print("="*15, "LOJA DIANA","="*15)
valor = float(input("preço de pagamento? "))
opção = int(input(""" FORMAS DE PAGAMENTO 
[1] a vista em dinherio/cheque
[2] a vista no cartão 
[3] 2x no cartão     
[4] 3x ou mais no cartão 
Qual é a parcela?
"""))
if opção == 1: 
    novo_valor = valor - (valor*0.1)
    print(f"O valor da sua compra teve um desconto de 10% e o novo valor de pagamento é {novo_valor}")

if opção == 2: 
    novo_valor = valor - (valor*0.05)
    print(f"O valor da sua compra teve um desconto de 5% e o novo valor de pagamento é {novo_valor}")

if opção == 3:
    print(f"Sua parcela saira em um valor de 2x de {valor/2}")

if opção == 4:
    parcela = int(input('Quantas vezes ira dividir? '))
    juros = valor + (valor*0.2)
    print(f'''Seu valor teve um aumento de 20% \nseu novo valor é {juros} e sua parcela vai ser {parcela} de {juros/parcela}''')
