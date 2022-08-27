cidade = input("digite sua cidade ")
cidade = cidade.upper()
separa = cidade.split()

if separa[0] == "SANTOS" or separa[0] == "SANTO":
    print(True)
else:
    print(False)
