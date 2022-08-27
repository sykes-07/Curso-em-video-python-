casa = float(input("Qual o valor da casa? "))
salario = float(input("qual o salario "))
prestação = float(input('prestação de quantos anos? '))


porcentagem = salario*0.3
mes = 12*prestação
presta_mes = casa/mes

if presta_mes >= porcentagem:
    print("emprestimo negado")
else:
    print("emprestimo concedido") 

print(f"{presta_mes:.2f}")
