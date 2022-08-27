cont = "S"
jogador = {}
partida = []
while cont == "S":
    jogador["nome"] = input("qual o nome do jogador? ")
    total = int(input(f'uantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, total):
        gol = int(input(f"quantos gols na partida {i+1}? "))
        partida.append(gol)
    jogador["gols"] = partida[:]
    jogador["total"] = sum(partida)
    cont = input("deseja contimuar? ").upper()

print(jogador)
for k, a in jogador.items():
    print(f'o campo {k} tem o valor {a}')
print("=" *30)

print("="*30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for e, r in enumerate(jogador["gols"]):
    print(f'    => na partida {e} fez {r} gols ')









