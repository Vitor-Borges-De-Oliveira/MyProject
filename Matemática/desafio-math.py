# A solução do desafio, aula 3

# Celsius para Fahrenheit
# F = (C * 1.8) + 32

# Celsius para Kelvin
# TK = TC + 273.15

# Kelvin para Celsius
# C = K - 273.15

# Kelvin para Fahrenheit
# F = (K - 273.15) * 1.8 + 32

# Fahrenheit para Celsius
# C = (F - 32) / 1.8

# Fahrenheit para Kelvin
# K = (F + 459.67) * 1.8

c = int(input("Digite a temperatura em Celsius: "))
f = int(input("Digite a temperatura em Fahrenheit: "))
k = int(input("Digite a temperatura em Kelvin: "))

cf = (c * 1.8) + 32
ck = c + 273.15
kc = k - 273.15
kf = (k - 273.15) * 1.8 + 32
fc = (f - 32) / 1.8
fk = (f + 459.67) * 1.8

print(f"O valor de {c}º Celsius para Fahrenheit é: {cf}")
print(f"O valor de {c}º Celsius para Kelvin é: {ck}")
print(f"O valor de {k}º Kelvin para Celsius é: {kc}")
print(f"O valor de {k}º Kelvin para Fahrenheit é: {kf}")
print(f"O valor de {f}º Fahrenheit para Celsius é: {fc}")
print(f"O valor de {f}º Fahrenheit para Kelvin é: {fk}")