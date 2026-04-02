# Exercício 1, dia 01/04/2026
numeros = [[1, 2],
           [3, 4]]

somar = int(input("Digite o somador: "))

for x in range(0, 2):
    for y in range(0, 2):
        numeros[x][y] = numeros[x][y] + somar

print(f"A soma dos números é: {somar}")
print("Resultado das operações: ")
for resultado in numeros:
    print(resultado)