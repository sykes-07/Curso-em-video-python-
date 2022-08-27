#largura e altura
#dimensão, area e litros 

largura = float(input("qual a largura da parede? "))
altura = float(input("qual é a altura da parede?"))

area = largura*altura
litros = area/2


print(f"sua dimensão é{largura}X{altura} e sua area é {area}")
print(f"é necessario para pintar a parede {litros} litros de tinta ")