# Demonstração de funções em listas:
print("Eis, os meus maiores sonhos: ")
sonhos = ["1. Me divertir na Disney",
          "2. Me banhar na praia de Sepetiba",
          "3. Tirar as férias em Paris",
          "4. Fazer compras no WestShopping",
          "5. Ver as pirâmides do Egite"]
for x in sonhos:
    print(x)

print("Ops, não quero Sepetiba!")
del(sonhos[1])
print("E nem WestShopping")
del(sonhos[3])

print("Conferindo os sonhos...")
for x in sonhos:
    print(x)