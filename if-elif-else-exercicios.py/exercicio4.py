# Exercício 4, dia 04/03/2026
time = input("Digite o nome do seu time: ")
print("Cadastre a posição do time abaixo: ")
print("Campeão! (1º lugar)")
print("Libertadores! (entre 2º e 6º)")
print("Sul-Americana! (entre 7º e 12º)")
print("Rebaixado! (entre os 4 últimos)")
posicao = int(input())

if posicao:
    if posicao == 1:
        print(f"{time} é Campeão!")
    elif posicao > 1 and posicao <= 6:
        print(f"{time} é Libertadores!")
    elif posicao > 6 and posicao <= 12:
        print(f"{time} é Sul-Americana!")
    else:
        print(f"{time} foi Rebaixado!")
else:
    print("Você deve informar uma posição")