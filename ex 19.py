import math
co  = float(input("me diga o cateto oposto "))
ca = float(input("me diga o cateto adjacente "))
hip = math.hypot(co, ca)
print(f"a hipotenusa é {hip:.2f}")
