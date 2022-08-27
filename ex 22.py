nome = input("digite seu nome: ").strip()#tirar os epaços 
print(f"maiusculo é {nome.upper()}")
print(f"minusculo {nome.lower()} ")
separa = nome.split()#lista com os nomes    
print(f"primeiro nome {separa[0]} e as letra é {len(separa[0])}")