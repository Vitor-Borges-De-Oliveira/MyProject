# Demonstração do uso de funções 2:
def adicao(x, y):
    w = x + y
    return w
def subtracao(x, y):
    return x - y

print("Digite dois valores inteiros: ")
n1 = int(input("X: "))
n2 = int(input("Y: "))
op = input("Qual operação (+ ou -)?")

if op == "+":
    z = adicao(n1, n2)
    print(f"Resultado da soma: {z}")
elif op == "-":
    z = subtracao(n1, n2)
    print(f"Resultado da subtração: {z}")
else:
    print("Opção digitada inexistente!")