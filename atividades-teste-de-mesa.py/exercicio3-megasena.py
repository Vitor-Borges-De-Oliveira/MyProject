# Exercício 3, dia 18/03/2026
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))
num6 = int(input("Digite o sexto número: "))

if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or num1 == num6:
    print("Por favor, digite números diferentes!")
elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5 or num2 == num6:
    print("Por favor, digite números diferentes!")
elif num3 == num2 or num1 == num3 or num3 == num4 or num3 == num5 or num3 == num6:
    print("Por favor, digite números diferentes!")
elif num4 == num2 or num4 == num3 or num1 == num4 or num4 == num5 or num4 == num6:
    print("Por favor, digite números diferentes!")
elif num5 == num2 or num5 == num3 or num5 == num4 or num1 == num5 or num5 == num6:
    print("Por favor, digite números diferentes!")
elif num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5 or num6 == num1:
    print("Por favor, digite números diferentes!")
else:
    print(f"Os números são: {num1}, {num2}, {num3}, {num4}, {num5}, {num6}!")