# Exercício 3, dia 01/04/2026
tarefas = []

for x in range(0, 5):
    fazer = input(f"Digite a {x+1}ª tarefa: ")
    tarefas.append(fazer)

print("Segue a lista de tarefas: ")
for y in tarefas:
    print(y)

while True:
    print("Eis, a tarefa que está no topo da lista: ")
    print(tarefas[0])
    resposta = input("Você já fez esta tarefa (S/N)?")
    if resposta == "S":
        del(tarefas[0])
        fazer = input("Digite a nova tarefa: ")
        tarefas.append(fazer)
    else:
        break
print("Segue a lista atualizada: ")
for y in tarefas:
    print(y)