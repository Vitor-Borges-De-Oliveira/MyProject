# Exercício 1, dia 30/03/2026
print("Questões: ")
questoes = ["1. Questão 1",
            "2. Questão 2",
            "3. Questão 3",
            "4. Questão 4",
            "5. Questão 5"]
respostas = []

for x in questoes:
    print(x)
    resposta = input("Insira a resposta: ").upper()
    respostas.append(resposta)

gabarito = ["B", "C", "A", "E", "D"]

for i in range(0, 5):
    if respostas[i] == gabarito[i]:
        print("Respostas corretas!")
    else:
        print("Respostas erradas!")