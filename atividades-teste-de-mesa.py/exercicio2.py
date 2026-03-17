# Exercício 2, dia 16/03/2026
print("Insira os dados: ")

nome = input("Nome: ")
nasc= input("Data de nascimento: ")
sexo = input("Sexo: ")
diag = input("Diagnóstico: ")
estado = input("Estado: ")
trat = input("Tratamento: ")
libera = input("Data de liberação: ")

print("\n1 - Ver dados")
print("2 - Alterar dados")

opcao = int(input("Digite uma opção: "))

if opcao == 1:
    print("\nDados do paciente: ")
    print(f"Nome: {nome}")
    print(f"Data de nascimento: {nasc}")
    print(f"Sexo: {sexo}")
    print(f"Diagnóstico: {diag}")
    print(f"Estado: {estado}")
    print(f"Tratamento: {trat}")
    print(f"Data de liberação: {libera}")
elif opcao == 2:
    nome = input("Nome: ")
    nasc= input("Data de nascimento: ")
    sexo = input("Sexo: ")
    diag = input("Diagnóstico: ")
    estado = input("Estado: ")
    trat = input("Tratamento: ")
    libera = input("Data de liberação: ")
else:
    print("Por favor, digite uma opção válida.")