# Exercício 5, dia 04/03/2026
x = int(input("Digite o número de X: "))
y = int(input("Digite o número de Y: "))
z = int(input("Digite o número de Z: "))

if x < y and y < z:
    print(f"Os números {x}, {y}, e {z} estão na ordem crescente!")
elif z < x and z < y:
    print(f"Os números {x}, {y}, e {z} estão na ordem decrescente!")
else:
    print("Eles estão misturados!")