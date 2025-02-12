import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print('Bem-vindo ao PyPassword Generator!')
qtd_letras = int(input('Quantas letras você gostaria em sua senha?\n'))
qtd_simbolos = int(input('E quantos símbolos?\n'))
qtd_numeros = int(input('E quantos números?\n'))

# senha = ''
lista_senha = []

# for letra in range(1, qtd_letras + 1):
for letra in range(0, qtd_letras):
    # lista_senha += random.choice(letras)
    lista_senha.append(random.choice(letras))

# for simbolo in range(1, qtd_simbolos + 1):
for simbolo in range(0, qtd_simbolos):
    # lista_senha += random.choice(simbolos)
    lista_senha.append(random.choice(simbolos))

# for numero in range(1, qtd_numeros + 1):
for numero in range(0, qtd_numeros):
    # lista_senha += random.choice(numeros)
    lista_senha.append(random.choice(numeros))

random.shuffle(lista_senha)

# senha = ''
# for caractere in lista_senha:
#     senha += caractere
senha = ''.join(lista_senha)

print(f'Sua senha é: {senha}')