# Autor: Michael Douglas
# Data: 29/10/2026
# Linguagem: Python

def classificar_partidas(vitorias, derrotas):
    saldo = vitorias - derrotas

    niveis = [
        (10, "Ferro"),
        (20, "Bronze"),
        (50, "Prata"),
        (80, "Ouro"),
        (90, "Diamante"),
        (100, "Lendário")
    ]

    for limite, nivel in niveis:
        if vitorias <= limite:
            return saldo, nivel

    return saldo, "Imortal"


nome = input("Digite o nome do Herói: ")

while True:
    try:
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))

        if vitorias < 0 or derrotas < 0:
            print("Os valores não podem ser negativos.")
            continue

        break

    except ValueError:
        print("Por favor, digite apenas números inteiros.")


saldo_vitorias, nivel = classificar_partidas(vitorias, derrotas)

print(f"O Herói {nome} tem de saldo de {saldo_vitorias} e está no nível de {nivel}.")
