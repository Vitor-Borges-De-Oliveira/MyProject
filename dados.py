# Demonstração de variáveis
nome = "Vitor Borges de Oliveira" # Exemplo de string
altura = 1.60                     # Exemplo de float
idade = 27                        # Exemplo de inteiro
naturalidade = "Brasileiro"
cor_cabelo = "Preto"
cor_olhos = "Preto"
raca = "Caucasiano"
conjuge = "error!"
filhos = "error!"
jogo = "do bicho"
emprego = "vagabundo"
status = "AFK base"
dps = 20




# Exibição do conteúdo das variáveis...
print("Meu nome é", nome,)
print("A minha altura é", altura, "metros.")
print("Minha idade é", idade, "anos.")
print("Naturalidade", naturalidade)
print("Cor dos cabelos:", cor_cabelo)
print("Cor dos olhos:", cor_olhos)
print("Raça:", raca)
print("Nome da cônjuge:", conjuge)
print("Número de filhos", filhos)
print("Jogo", jogo)
print("Emprego atual:", emprego)
print("Status atual:", status)
print("Dano por segundo", dps)

# Inputação de dados em variáveis...
print("Digite o seu nome: ")
nome1 = str(input())

print("Digite sua altura: ")
altura1 = float(input())

print("Digite sua idade: ")
idade1 = int(input())

print("Seu nome é", nome1, "sua altura é de", altura1,"e você possui", idade1, "anos")

print(type(nome1))
print(type(altura1))
print(type(idade1))
