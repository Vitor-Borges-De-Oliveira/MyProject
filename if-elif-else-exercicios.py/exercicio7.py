# Exercício 7, dia 04/03/2026
print("Insira sua função: ")
print("Goleiro")
print("Zagueiro")
print("Lateral")
print("Ala")
print("Volante")
print("Meia")
print("Ponta")
print("Atacante")
print("Centroavante")
func = str(input())

if func:
    if func == "Goleiro" or func == "Zagueiro" or func == "Lateral":
        print("Defesa!")
    elif func == "Ala" or func == "Volante" or func == "Meia":
        print("Meio-Campo!")
    elif func == "Ponta" or func == "Atacante" or func == "Centroavante":
        print("Ataque!")
    else:
        print("Teimoso!")
else:
    print("Você deve inserir sua função!")