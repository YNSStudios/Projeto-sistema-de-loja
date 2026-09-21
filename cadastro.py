import json
from time import sleep

try:
    with open("clientes.json", "r", encoding="utf-8") as dados:
        clientes = json.load(dados)
except FileNotFoundError:
    clientes = []

try:
    with open("produtos.json", "r", encoding="utf-8") as dados:
        produtos = json.load(dados)

except FileNotFoundError:
    produtos = []

print("[1] Login")
print("[2] Cadastrar")
print()

while True:
    escolha = input("O que vai fazer: ")
    print()

    try:
        escolha = int(escolha)
        break
    except ValueError:
        print("Acho que algo deu errado :(. Tente novamente !")
        print()

if escolha == 1:

    print("\033[33mÁrea de login.\033[0m")
    print()

    while True:

        nome_usuario = input("Digite seu nome de usuário: ")
        print()

        usuario_encontrado = None

        for usuario in clientes:
            if usuario["nome"] == nome_usuario:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is not None:
            break
        else:
            print("\033[31mUsuário não encontrado ! tente novamente.\033[0m")
            print()

elif escolha == 2:

    print("\033[33mÁrea de cadastro.\033[0m")
    print()

    while True:

        print("\033[0mDigite um nome com mais de 8 caracteres, e com números, o nome não deve conter caracteres especiais. \033[0m")
        print()

        nome_usuario = input("Digite um nome de usuário válido: ")
        print()

        if len(nome_usuario) >= 8:

            usuario_encontrado = None

            for usuario in clientes:
                if usuario["nome"] == nome_usuario:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado is not None:
                print("\033[31mNome já em uso, tente outro !\033[0m")
                print()

            else:
                break

        else:
            print("\033[31mDigite um nome com mais de 8 caracteres.\033[0m")
            print()