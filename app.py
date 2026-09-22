import json
import random
from time import sleep

try:
    with open("produtos.json", "r", encoding="utf-8") as dados:
        produtos = json.load(dados)

except FileNotFoundError:
    produtos = []


def verificação_de_numeros():

    while True:

        valor = input("\033[33mdigite aqui: \033[0m").replace(",", ".")

        try:

            valor = float(valor)
            return valor

        except ValueError:

            erro = "\033[31mValor inválido. \033[0m"
            print(erro)


sleep(0.6)

print("=================")
print("[1] Criar produtos")
print()
print("[2] Editar produtos")
print()
print("[3] Remover produtos")
print()
print("[4] Visuzlizar produtos")
print()

escolha = int(verificação_de_numeros())
print()

if escolha == 1:

    print("\033[33mCriação de produtos !\033[0m")
    print()

    print("Digite quantos produtos você ira cadastrar. ")

    qtd_produtos = int(verificação_de_numeros())
    print()

    for c in range(qtd_produtos):

        while True:

            codigo = random.randint(1000, 9999)

            codigo_encontrado = None

            for produto in produtos:
                if produto["codigo"] == codigo:
                    codigo_encontrado = True
                    break

            if codigo_encontrado == None:
                break

        nome = input("Digite o nome do produto: ").title().strip()
        print()
        print("Apenas números. ")
        print()

        print("Digite o valor do produto. ")
        preço = verificação_de_numeros()
        print()

        print("Digite o estoque do produto. ")
        estoque = int(verificação_de_numeros())
        print()

        classe = (
            input("o que é seu produto ? eletrônico, domestico ... : ")
            .capitalize()
            .strip()
        )
        print()

        produtos.append(
            {
                "nome": nome,
                "preço": preço,
                "estoque": estoque,
                "classe": classe,
                "codigo": codigo,
            }
        )

        print("\033[32mProduto criado !\033[0m")
        print()

    with open("produtos.json", "w", encoding="utf-8") as dados:
        json.dump(produtos, dados, ensure_ascii=False, indent=5)

elif escolha == 2:

    print("\033[33mEdição de produtos !\033[0m")
    print()

    for produto in produtos:
        sleep(0.5)
        print(f"nome: {produto['nome']}")
        print(f"Código: {produto['codigo']}")
        print()
        sleep(0.5)

    while True:
        print("Digie o código do produto. ")
        codigo_busca = verificação_de_numeros()
        print()

        produto_encontrado = None

        for produto in produtos:
            if produto["codigo"] == codigo_busca:
                produto_encontrado = produto
                break

        if produto_encontrado is not None:
            print("\033[32mProduto encontrado !\033[0m")
            print()
            break
        else:
            print("\033[31mProduto não encontrado !\033[0m")

    print(f"Nome: {produto_encontrado['nome']}")
    print(f"Estoque: {produto_encontrado['estoque']}")
    print(f"Preço: R${produto_encontrado['preço']}")
    print()

    print("O que você vai editar: Nome, Estoque, Preço ? ")
    print()

    while True:

        ediçao = input("Digite aqui: ").lower().strip()
        print()

        if ediçao == "nome":

            novo_nome = input("Digite o novo nome: ").title().strip()
            produto_encontrado["nome"] = novo_nome
            break

        elif ediçao == "estoque":
            print("Digite o estoque do produto. ")
            novo_estoque = int(verificação_de_numeros())
            produto_encontrado["estoque"] = novo_estoque
            break

        elif ediçao == "preço":
            print("Digite o preço. ")
            novo_preço = verificação_de_numeros()
            produto_encontrado["preço"] = novo_preço
            break

        else:
            print("\033[31mOpção inválida ! tente novamente. \033[0m")

    with open("produtos.json", "w", encoding="utf-8") as dados:
        json.dump(produtos, dados, ensure_ascii=False, indent=5)

        print()
        print(f"Nome: {produto_encontrado['nome']}")
        print(f"Estoque: {produto_encontrado['estoque']}")
        print(f"Preço: R${produto_encontrado['preço']}")
        print()

        print("\033[32mProduto editado com sucesso !\033[0m")
        print()

elif escolha == 3:

    print("\033[33mRemoção de produto\033[0m")
    print()

    for produto in produtos:
        print("=====================")
        print(f"Nome: {produto['nome']}")
        print(f"Código: {produto['codigo']}")
        print()

    while True:

        print("Digite o codigo do produto que deseja remover")
        remover = int(verificação_de_numeros())
        print()

        produto_remoçao = None

        for produto in produtos:
            if produto["codigo"] == remover:
                produto_remoçao = produto
                break

        if produto_remoçao is not None:
            break
        else:
            print("\033[31mProduto não encontrado !\033[0m")
            print()

    produtos.remove(produto_remoçao)

    with open("produtos.json", "w", encoding="utf-8") as dados:
        json.dump(produtos, dados, ensure_ascii=False, indent=5)

    print("\033[32mProduto removido com sucesso !\033[0m")
    print()

elif escolha == 4:

    print("\033[33mVizualizar produtos\033[0m ")
    print()

    for produto in produtos:

        sleep(0.5)
        print("==================")
        sleep(0.5)
        print(f"Nome: {produto['nome']}")
        sleep(0.5)
        print(f"Preço: R${produto['preço']}")
        sleep(0.5)
        print(f"Estoque: {produto['estoque']}")
        print()
        sleep(0.5)


else:
    print("\033[31mOpção inválida, tente novamente !\033[0m")
    print()
