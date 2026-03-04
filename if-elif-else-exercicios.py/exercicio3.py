# Exercício 3, dia 02/03/2026
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

print(f"Você possui {peso}kg e mede {altura}cm")

if imc > 25:
    print("Você está acima do peso ideal!")

elif imc < 18:
    print("Você está abaixo do peso ideal!")

else:
    print("O seu peso está OK!")