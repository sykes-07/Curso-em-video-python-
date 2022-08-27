ano  = int(input("ano de nasciemento "))

idade = 2022-ano

if idade < 18:
    anoo = 18 - idade 
    anooo = anoo + 2022 
    print(f"a idade dele é {idade} em 2022 \nAinda faltam {anoo} anos para se alistar\nSeu alistamento vao ser em {anooo} ")

elif idade == 18:
    print("DEVE FAZER O ALISTAMENTO IMEDIATAMENTE")

else:
    ano2 = idade - 18
    ano3 = 2022 - ano2
    print(f"tem {idade} anos\ndeveria ter se alistado a {ano2} atras em {ano3} ")
