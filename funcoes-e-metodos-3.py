# Demonstração de métodos em listas:
inss = ["Maria", "Manoel", "José", "Isabela"]
print(f"Eis, a fila do INSS: {inss}")

novo = input("Insira mais uma pessoa: ")
inss.append(novo)
print(f"Conferindo a nova lista: {inss}")

print("Vou tirar a última pessoa desta lista: ")
especial = inss.pop()

print("Agora vou colocá-la na frente de todos!")
inss.insert(0, especial)
print(f"Conferindo a a lista: {inss}")

print("Maria não gostou e reclamou...")
inss.remove("Maria")
print(f"E agora ela saiu 'pê da vida': {inss}")

print("Para não ter mais reclamação, vamo atender...")
inss.sort()
print(f"... em ordem alfabética: {inss}")

print(f"Onde esta a nova pessoa chamada {especial}?")
print(f"Ela agora ficou na posição {inss.index(especial)+1}!")