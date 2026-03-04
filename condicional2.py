# Demonstração de operadores lógicos em condicionais:
manha = input("O que você irá fazer amanhã de manhã?")
tarde = input("O que você irá fazer amanhã à tarde?")

if not manha or not tarde:
    print("Você precisa dizer o que vai fazer!")
else:
    if manha == "jogar" and tarde == "dormir":
        print("Você está desperdiçando o seu dia!")
    elif manha == "dormir" and tarde == "jogar":
        print("Você está desperdiçando o seu dia!")
    elif manha == "estudar" and tarde == "treinar":
        print("Parabéns, você está no caminho certo!")
    elif manha == "treinar" and tarde == "estudar":
        print("Parabéns, você está no caminho certo!")
    elif manha == "jogar" and tarde == "estudar":
        print("Tudo bem, poderia ser melhor, mas já é um começo!")
    elif manha == "estudar" and tarde == "jogar":
        print("Tudo bem, poderia ser melhor, mas já é um começo!")
    elif manha == "dormir" and tarde == "treinar":
        print("Tudo bem, poderia ser melhor, mas já é um começo!")
    elif manha == "treinar" and tarde == "dormir":
        print("Tudo bem, poderia ser melhor, mas já é um começo!")
    else:
        print("Você não me respondeu...")