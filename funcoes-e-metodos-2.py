# Demonstração de funções em listas:
numeros = [7, 2, 9, 6, 5, 0, 3, 8, 1, 4]
palavras = ["olá", "alô", "hei", "uau", "ops"]

print("Quantas variáveis possui: ")
print(f"Números: {len(numeros)}")
print(f"Palavras: {len(palavras)}")

print("Vamos reordenar essas listas?")
print(sorted(numeros))
print(sorted(palavras))

print(f"O somatório de números: {sum(numeros)}")
print(f"O maior valor é: {max(numeros)}")
print(f"A primeira palavra é: {min(palavras)}")