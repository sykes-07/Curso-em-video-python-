from random import choice
lista =  []

quant= int(input("quantos aulunos são? "))
for i in range(0, quant):
    nome = input("quanl o nome do aluno ")
    lista.append(nome)

alea = choice(lista)
print(alea)