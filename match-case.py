# Demonstração do uso da condicional match/case:
print("Digite o número referente ao estado da moeda: ")
print("1. Flor de cunho")
print("2. Soberba")
print("3. Muito bem conservada")
print("4. Bem conservada")
print("5. Outros estados")
estado = int(input())

match estado:
    case 1:
        print("Beleza! Vou pagar 1kk")
    case 2:
        print("De boa! Vou pagar 250k")
    case 3:
        print("Muito pika! Posso dar uns 100k")
    case 4:
        print("Daora, mas você aceitaria 30k?")
    case 5:
        print("Mals aí, não gostei")
    case _:
        print("É o quê?")