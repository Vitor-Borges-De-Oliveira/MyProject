# Demonstração do uso de if:
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
    print("Não poderá realizar operações bancárias!")

elif idade >= 65:
    print("Você já é aposentado!")
    print("Poderemos oferecer suporte técnico...")

else:
    print("Você é maior de idade.")
    print("Portanto, poderá escolher os nossos serviços!")

print("Obrigado por escolher os nossos serviços")

