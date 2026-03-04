# Exercício extra 2, dia 02/03/2026
print("Digite um dia da semana: ")
print("1. Domingo")
print("2. Segunda-feira")
print("3. Terça-feira")
print("4. Quarta-feira")
print("5. Quinta-feira")
print("6. Sexta-feira")
print("7. Sábado")
fazer = int(input())

match fazer:
    case 1:
        print("Domingo é dia de descansar e ir à igreja!")
    case 2:
        print("Segunda-feira é dia de sofrer!")
    case 3:
        print("Na terça-feira a dor é invevitável, mas o sofrimento é opcional!")
    case 4:
        print("Quase lá! Quarta-feira a gente começa a sonhar!")
    case 5:
        print("Já estou me sentindo melhor! Quinta-feira é mais ou menos, mas ainda é melhor que ontem!")
    case 6:
        print("SEXTOU!")
    case 7:
        print("Sábado é dia do baiano! Não me acorda!")
    case _:
        print("Dia inexistente! Você ultrapassou os limites...")