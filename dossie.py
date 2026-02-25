# Inputação de dados do dossiê
print("Digite o jogo que você joga: ")
jogo = str(input())

print("Digite o seu nick: ")
nick = str(input())

print("Digite o elo em que você está: ")
elo = str(input())

print("Digite o seu personagem: ")
personagem = str(input())

print("Digite seu nível: ")
nivel = int(input())

print("Digite sua taxa de K/D: ")
kd = float(input())

print("Digite a naturalidade de seu personagem: ")
naturalidade = str(input())

print("Digite sua função no jogo: ")
funcao = str(input())

print("Digite seu status atual: ")
status = str(input())


print("O jogo que você joga é", jogo, ", seu nick é", nick, ", seu elo é", elo, ", seu personagem se chama", personagem, ", seu nível é", nivel, ", sua taxa de K/D é de", kd,
       ", a naturalidade de seu personagem é", naturalidade, ", a função de seu personagem dentro do jogo é", funcao, "e", status, "é seu status atual.")

print(type(jogo))
print(type(nick))
print(type(elo))
print(type(personagem))
print(type(nivel))
print(type(kd))
print(type(naturalidade))
print(type(funcao))
print(type(status))

