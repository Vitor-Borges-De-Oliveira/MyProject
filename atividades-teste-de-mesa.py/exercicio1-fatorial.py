# Exercício 1, dia 16/03/2026
n = int(input("Digite o valor: "))
f = 1

if n < 0 or n > 25:
    print("O número inserido não pode ser menor que 0 ou maior que 25. Tente de novo!")
else:   
    for x in range(1, n+1):
        f = f * x
        print(f"O fatorial de {n} é {f}")