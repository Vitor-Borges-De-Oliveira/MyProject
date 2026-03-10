# Exercício 4, dia 09/03/2026
x = 0
y = 1

while x <= 2000:
    print(x)
    x, y = y, x + y
print(f"Próximo número da sequência: {x}")