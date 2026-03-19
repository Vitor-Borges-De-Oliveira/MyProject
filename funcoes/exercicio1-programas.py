# Exercício 1, dia 18/03/2026
def pessoa():
    print(f"Meu nome é {nome} e tenho {idade} anos.")
    return
def conferir(x):
    if x >= 18:
        print("Você é maior de idade, portanto aqui está uma lista de carros e seus preços: ")
        print("Remington - R$4000,00")
        print("Sabre - R$3000,00")
        print("Turismo - R$50000,00")
        print("Clove - R$2500,00")
        print("Tahoma - R$12000,00")
        print("Euros - R$25000,00")
    else:
        print("Você é menor de idade, portanto aqui vão alguns programas infantis: ")
        print("Teletubbies")
        print("Josnei")
        print("FunkyBlackCat")
        print("A Volta dos VASPS")
        return

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

pessoa()
conferir(idade)