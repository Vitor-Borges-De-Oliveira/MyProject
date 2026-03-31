# Demonstração de acesso a listas:
print("Vou montar a marmita com 5 alimentos!")
marmita = ["feijão", "arroz", "legumes", "salada", "carne"]
print(f"Eis a nossa recomedação: {marmita}")

resposta = input("Quer montar uma marmita diferente (S/N?)")
if resposta == "S":
    for x in range(len(marmita)):
        print(f"Digite o {x+1}º item do cardápio:")
        marmita[x] = input()
    print(f"A marmita montada foi: {marmita}")
    print(f"Os três primeiros itens foram: {marmita[0:3]}")
    print(f"O último item da marmita foi: {marmita[-1]}")
else:
    print("Ok, você decide...")