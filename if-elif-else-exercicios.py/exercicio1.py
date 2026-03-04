# Exercício 1, dia 02/03/2026
saldo = int(input("Informe o salde de sua conta: "))
valorprod = int(input("Informe o valor do produto: "))

falta = valorprod - saldo
extra = saldo - valorprod

print(f"Você possui R${saldo} e o produto custa R${valorprod}")

if saldo >= valorprod:
    print("Você possui o suficiente para comprar o produto!")
    print(f"Vão sobrar R${extra} ao concluir a compra!")

elif saldo < valorprod:
    print("Você não tem o suficiente para comprar este produto!")
    print(f"Faltam R${falta} para concluir a compra!")
