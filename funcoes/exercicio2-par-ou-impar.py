# Exercício 2, dia 18/03/2026
import random

# Função para gerar o número do PC:
def numero_pc():
    return random.randint(0, 10)

# Função para verificar o resultado:
def resultado(jogador, pc):
    soma = jogador + pc

    print(f"\nO jogador digitou {jogador}")
    print(f"O PC digitou {pc}")
    print(f"A soma é {soma}")

    if soma % 2 == 0:
        print("Resultado: PAR!")
        print("Jogador wins!")
    else:
        print("Resultado: ÍMPAR!")
        print("PC wins!")

# Função principal do jogo:
def jogo():
    print("= = = > JOGO PAR OU ÍMPAR < = = =")
    jogador = int(input("Digite um número: "))
    pc = numero_pc()

    resultado(jogador, pc)

# Executar jogo:
jogo()