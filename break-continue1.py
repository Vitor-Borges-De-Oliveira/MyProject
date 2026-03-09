# Demonstração de estrutura repetitiva:
contador = 0
senha = ""

while senha != "coxinha123":
    print("Digite a senha: ")
    senha = input()

    if senha == "coxinha123":
        print("Senha correta!")
        break
    else:
        print("Senha errada!")

    contador += 1
    if contador == 3:
        print("3 tentativas excedidas!")
        break