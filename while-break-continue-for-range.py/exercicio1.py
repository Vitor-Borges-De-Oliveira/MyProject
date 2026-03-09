# Exercício 1, dia 09/03/2026
print("Digite um número: ")
num = int(input())

print(f"Tabuada de {num}: ")
for x in range (0, num+1):
    calc = x * num
    print(f"{x} X {num} = {calc}")