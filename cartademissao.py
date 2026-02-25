# Exemplo de carta de demissão.
print("Digite o nome da empresa: ")
empresa = str(input())

print("Digite o nome do seu gestor: ")
gestor = str(input())

print("Digite seu cargo atual: ")
cargo = str(input())

print("Digite a data de início do aviso prévio: ")
data_inicio = str(input())

print("Digite a data do término do aviso prévio: ")
data_final = str(input())

print("Digite o local onde você trabalha e a data do envio: ")
local_data = str(input())

print("Digite sua assinatura: ")
assinatura = str(input())

print("Digite seu nome completo: ")
nome = str(input())

print(f"À {empresa}. \n\nPrezado(a) {gestor}. \n\nVenho por meio desta carta comunicar formalmente meu pedido de demissão do cargo de {cargo}. \n\nEstarei à disposição da empresa durante o aviso prévio, no período de {data_inicio} a {data_final}. \n\n{local_data}. \n{assinatura}. \n{nome}")