lado1 = float(input('Qual o primeiro lado? '))
lado2 = float(input('Qual o segundo lado? '))
lado3 = float(input('Qual o terceiro lado? '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("triangulo EQUILATERO")

    elif lado1 != lado2 != lado3:
        print("triangulo ESCALENO")
    else:
        print("triangulo ISOSCELES")

else:
    print("Triangulo não pode ser feito")
     