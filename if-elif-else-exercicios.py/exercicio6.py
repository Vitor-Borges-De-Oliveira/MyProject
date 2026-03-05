# Exercício 6, dia 04/03/2026
l1 = float(input("Informe o tamanho do lado 1 do triângulo: "))
l2 = float(input("Informe o tamanho do lado 2 do triângulo: "))
l3 = float(input("Informe o tamanho do lado 3 do triângulo: "))

equ = l1 == l2 == l3
iso = l1 == l2 or l2 == l3 or l1 == l3
esc = l1 != l2 != l3

if l1 == l2 == l3:
    print(f"O lado 1 mede {l1}, o lado 2 mede {l2} e o lado 3 mede {l3}. Este triângulo é Equilátero!")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print(f"O lado 1 mede {l1}, o lado 2 mede {l2} e o lado 3 mede {l3}. Este triângulo é Isósceles!")
else:
    print(f"O lado 1 mede {l1}, o lado 2 mede {l2} e o lado 3 mede {l3}. Este triângulo é Escaleno!")
