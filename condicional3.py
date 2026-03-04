# Demonstração de condicionais e operadores:
avaliacao = input("Digite a nota: ")

if avaliacao:
    if avaliacao.upper() == "A" or avaliacao == "B" or avaliacao == "C":
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Você não digitou!")