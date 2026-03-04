# Exercício 2, dia 02/03/2026
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f"Sua média é {media}!")
    print("Aluno aprovado!")
else:
    print(f"Sua média é {media}!")
    print("Aluno reprovado!")

