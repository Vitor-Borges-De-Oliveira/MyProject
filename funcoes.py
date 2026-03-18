# Demonstração do uso de funções:
def apresentar():
    print(f"Meu nome é {nome}.")
    print(f"Minha altura é {altura}m.")
    print(f"Minha idade é {idade} anos.")
    return
def conferir(x):
    if x >= 18:
        print("Você é maior de idade!")
    else:
        print("Menor de idade! LEI FELCA!")
        return
    
nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

apresentar()
conferir(idade)