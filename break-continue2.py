# Demonstração do uso da estrutura repetitiva parte 2:
num = 1
while num >= 0:
    print("Digite um número negativo para sair: ")
    num = int(input())
    continue
    print("Este texto não será exibido! Mas...")
else:
    print(f"O número digitado foi: {num}")