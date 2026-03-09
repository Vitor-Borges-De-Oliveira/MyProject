# Exercício 8, dia 04/03/2026
print("Por favor informe se o serviço foi prestado de maneira correta: ")
print("Digite (1) para Sim")
print("Digite (2) para Não")
servico = int(input())

if servico == 1:
    print("Por favor, avalie nossos serviços: ")
    print("(5) Ótimo!")
    print("(4) Bom!")
    print("(3) Razoável!")
    print("(2) Ruim!")
    print("(1) Péssimo!")
    ava = int(input())

    if ava == 1 or  ava == 2:
        print("Por favor, informe os motivos de sua reclamação: ")
        recl = str(input())
        if recl:
            print("Pedimos perdão pelo incoveniente. Estaremos felizes em corrigir nosso erro!")
        
elif servico == 2:
    print("Pedimos perdão pelo incoveniente. Estaremos felizes em corrigir nosso erro!")
else:
    print("Por favor, digite uma opção!")