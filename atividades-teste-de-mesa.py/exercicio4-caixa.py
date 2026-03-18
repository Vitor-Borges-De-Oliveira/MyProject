# Exercício 4, dia 18/03/2026
valor = float(input("Insira o valor: "))
cont50 = 0
cont20 = 0
cont10 = 0

while True:
    if valor >= 50:
        cont50 += 1
        valor = valor - 50
    elif valor >= 20:
        cont20 += 1
        valor = valor - 20
    elif valor >= 10:
        cont10 += 1
        valor = valor - 10
    else:
        break

print(f"Irei receber {cont50} notas de 50, {cont20} notas de 20 e {cont10} notas e 10")