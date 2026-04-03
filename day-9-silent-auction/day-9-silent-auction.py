from art import logo

print(logo)
print("Bem-vindo(a) ao programa de Leilão Secreto!")

lances = {}
continuar_lances = True


def registrar_lance(dicionario_lances):
    nome = input("Qual é o seu nome? ")
    valor = int(input("Qual é o seu lance? R$"))

    dicionario_lances[nome] = valor


def encontrar_maior_lance(dicionario_lances):
    maior_lance = 0
    vencedor = ""

    for licitante, lance in dicionario_lances.items():
        if lance > maior_lance:
            maior_lance = lance
            vencedor = licitante

    print(f"\nO vencedor é {vencedor} com um lance de R${maior_lance}!")


while continuar_lances:
    registrar_lance(lances)

    deve_continuar = input("Existem outros licitantes? Digite 'sim' ou 'não'.\n").lower()

    if deve_continuar == "sim":
        print("\n" * 100)
    elif deve_continuar in ("não", "nao"):
        continuar_lances = False
    else:
        print("Resposta inválida, assumindo que não há outros licitantes.")
        continuar_lances = False

encontrar_maior_lance(lances)
