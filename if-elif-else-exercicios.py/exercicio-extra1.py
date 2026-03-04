# Exercício extra 1, dia 02/03/2026
input(("Digite o programa de TV: "))
print("Digite a nota deste programa: ")
print("1. Ótimo!")
print("2. Bom!")
print("3. Razoável!")
print("4. Ruim!")
print("5. Péssimo!")
nota = int(input())

match nota:
    case 1:
        print("Ótimo!")
        print("Obrigado por nos avaliar!")
    case 2:
        print("Bom!")
        print("Obrigado por nos avaliar!")
    case 3:
        print("Razoável!")
        print("Obrigado por nos avaliar!")
    case 4:
        print("Ruim!")
        input("Digite o(s) motivo(s) de sua avaliação: ")
        print("Obrigado por nos avaliar!")
    case 5:
        print("Péssimo!")
        input("Digite o(s) motivo(s) de sua avaliação: ")
        print("Obrigado por nos avaliar!")
    case _:
        print("Nota inválida!")

