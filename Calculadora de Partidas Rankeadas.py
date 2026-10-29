# Autor: Michael Douglas
# Data: 29/10/2026
# Linguagem: Python

nome = (input("Digite o nome do Herói: "))

while True:
    try:
        partidas = int(input("Digite a quantidade de partidas jogadas: "))
        if partidas < 0:
            print("Quantidade de partidas inválida. O valor deve ser maior ou igual a 0.")
            continue
        break
    except ValueError:
        print("Quantidade de partidas inválida. Por favor, digite um número inteiro.")

    
def classificar_partidas(vitorias):
    if vitorias <= 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"
   

print(f"O Herói {nome} está no nível {classificar_partidas(partidas)}.")