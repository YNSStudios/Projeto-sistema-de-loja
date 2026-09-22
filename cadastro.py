import json
from random import randint
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


def verificação_de_numeros():

    while True:

        valor = input("\033[33mdigite aqui: \033[0m")

        try:

            valor = float(valor)
            return valor

        except ValueError:

            erro = "\033[31mValor inválido. \033[0m"
            print(erro)


def verificaçao_senha():

    while True:

        while True:

            senha = input("Digite uma senha forte: ")
            print()
            com_senha = input("Comfirme a senha: ")

            for verificar in senha:
                tem_letra = any(verificar.isalpha())
                tem_numero = any(verificar.isdigit())

            if tem_letra and tem_numero == True:
                break
            else:
                print("\033[31mEstá faltando uma letra ou número.\033[0m]")

        if senha == com_senha:
            print("Fassa uma senha forte com letras e números e caracteres especiais.")
            if len(senha) >= 8:
                if senha in [
                    "!",
                    "@",
                    "#",
                    "$",
                    "%",
                    "¨",
                    "&",
                    "*", 
                    "°",
                    "º",
                    "ª",
                    "£",
                    "¢",
                    "§",
                ]:
                    print("\033[32mSenha for te criada com sucesso.\033[0m")
                    print()

                    

                    return senha

                else:
                    print("Adicione um carácter especial. ")
            else:
                print("Asenha deve ter no minimo 8 caracteres. ")


print("[1] Login")
print("[2] Cadastrar")
print()

escolha = int(verificação_de_numeros())

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

        print(
            "\033[0mDigite um nome com mais de 8 caracteres, e com números, o nome não deve conter caracteres especiais. \033[0m"
        )
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

    print("Digite sua idade. ")
    idade = int(verificação_de_numeros())
    print()

    if idade >= 18:
        status = "Adulto"
    elif idade <= 17:
        status = "Menor de idade"

    senha = verificaçao_senha()

    cidade = input("Digite o nome da sua cidade: ")
    print()

    endereço = input("Dgite o nome da sua rua e bairro: ")
    print()

    numero_da_casa = int(verificação_de_numeros())

    while True:

        cep = int(verificação_de_numeros())

        if len(cep) == 8:
            break
        
    if status == "Menor de idade":

        nome_pai = input("Digite o nome do seu pai: ")
        nome_mae = input("Digite o nome da sua mãe: ")

        while True:

            codigo = randint(10000, 99999)

            semelhante = None

            for usuario in clientes:
                if usuario["codigo"] == codigo:
                    semelhante = usuario
                    break

            if semelhante in None:
                break

    else:

        nome_pai = None
        nome_mae = None

        while True:

            codigo = randint(10000, 99999)

            semelhante = None

            for usuario in clientes:
                if usuario["codigo"] == codigo:
                    semelhante = usuario
                    break

            if semelhante in None:
                break

    clientes.append(
        {
            "nome": usuario,
            "senha": senha,
            "idade": idade,
            "cidade": cidade,
            "endereço": endereço,
            "numemero da casa": numero_da_casa,
            "cep": cep,
            "nome_pai": nome_pai,
            "nome_mae": nome_mae,
            "Codigo": codigo,
        }
    )

    with open("clientes.json", "w", encoding="utf-8") as dados:
        json.dump(clientes, dados, ensure_ascii=False, indent=10)
