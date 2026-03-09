# Exercício 8, dia 04/03/2026
print("Por favor informe se o serviço foi prestado de maneira correta: ")
print("Digite (1) para Sim")
print("Digite (2) para Não")
servico = int(input())

if servico:
    if servico == 1:
        print("Por favor, avalie nossos serviços: ")
        print("(5) Ótimo!")
        print("(4) Bom!")
        print("(3) Razoável!")
        print("(2) Ruim!")
        print("(1) Péssimo!")
        ava = int(input())
    else:
        print("Por favor, informe os motivos de sua reclamação: ")
        motivos = input()
else:
    print("Obrigado por nos avaliar!")