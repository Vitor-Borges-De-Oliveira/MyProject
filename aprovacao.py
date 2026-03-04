"""
Eis as condições para o estudante ser aprovado:
NOTA: igual ou acima de 6; PRESENÇA: igual ou acima de 75%
Se uma das condições não forem satisfeitas, recuperação
Se nenhuma das condições não forem satisfeitas, reprovação.
"""

nota = int(input("Digite a nota: "))
presenca = int(input("Digite a presença: "))

if nota >= 6 and presenca >= 75:
    print("Aprovado!")
elif nota < 6 and presenca < 75:
    print("Reprovado!")
else:
    print("Recuperação!")