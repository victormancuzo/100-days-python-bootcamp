import string

from art import logo

alfabeto = list(string.ascii_lowercase)


def caesar(codificar_ou_decodificar, texto_original, quant_deslocamento):
    if codificar_ou_decodificar not in ("codificar", "decodificar"):
        print("Input inválido.")
        return
    # else:
    texto_saida = ""
    mensagem = "de" if codificar_ou_decodificar == "decodificar" else ""

    if codificar_ou_decodificar == "decodificar":
        quant_deslocamento *= -1

    for letra in texto_original:
        if letra in alfabeto:
            indice_deslocado = alfabeto.index(letra) + quant_deslocamento
            indice_deslocado %= len(alfabeto)
            texto_saida += alfabeto[indice_deslocado]
        else:
            texto_saida += letra

    print(f"Aqui está o resultado {mensagem}codificado: {texto_saida}")


print(logo)

while True:
    direcao = input("Digite 'codificar' para criptografar ou 'decodificar' para descriptografar:\n").lower()
    texto = input("Digite sua mensagem:\n").lower()
    deslocamento = int(input("Digite o número de deslocamento:\n"))

    caesar(codificar_ou_decodificar=direcao, texto_original=texto, quant_deslocamento=deslocamento)

    reiniciar = input("Digite 'sim' se quiser executar novamente. Caso contrário, digite 'não'.\n").lower()

    if reiniciar == "sim":
        continue
    elif reiniciar in ("nao", "não"):
        print("Ok, adeus!")
        break
    else:
        print("Input inválido, adeus!")
        break
