# Exercício 2, dia 01/04/2026
print("Lista de jogadores: ")
jogadores = []

for x in range(0, 11):
    jogador = input(f"Insira o nome do jogador {x+1}: ").upper()
    jogadores.append(jogador)

print("Segue a lista de jogadores: ")
for x in jogadores:
    print(f"Jogador número {x+1}: {jogador}")