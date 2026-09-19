import json
import random
from time import sleep

try:
    with open("produtos.json", "r", encoding="utf-8") as dados:
        produtos = json.load(dados)

except FileNotFoundError:
    produtos = []

sleep(0.6)

print("=================")
print("[1] Criar produtos")
print()
print("[2] Editar produtos")
print()

while True:
    escolha = input("Digite aqui: ")
    print()

    if escolha.isnumeric():
        escolha = int(escolha)
        break

    else:
        print("\033[31mIsso não é um número !\033[0m")
        print()

while True:

    if escolha == 1:

        print("\033[33mCriação de produtos !\033[0m")
        print()

        while True:

            qtd_produtos = input("Digite quantos produtos você vai cadastrar: ")
            print()
            if qtd_produtos.isnumeric():
                qtd_produtos = int(qtd_produtos)
                break
            else:
                print("Isso não é um número !")
                print()

        for c in range(qtd_produtos):

            while True:

                codigo = random.randint(1000, 9999)

                codigo_encontrado = None

                for produto in produtos:
                    if produto["codigo"] == codigo:
                        codigo_encontrado = True
                        break
                    elif produtos is None:
                        break

                if codigo_encontrado == None:
                    break

            nome = input("Digite o nome do produto: ").title().strip()
            print()
            print("Apenas números")
            print()
            preço = float(input("Digite o preço do produto: ").replace(",", "."))
            print()
            estoque = int(input("Digite o estoque do produto: "))
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

        break

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

            while True:

                codigo_busca = input("Digite o codigo do produto: ")
                print()
                if codigo_busca.isnumeric():
                    codigo_busca = int(codigo_busca)
                    break

            produto_encontrado = None

            for produto in produtos:
                if produto["codigo"] == codigo_busca:
                    produto_encontrado = produto
                    break

            if produto_encontrado is not None:
                print("\033[32mProduto encontrado !\033[0m")
                print()
                break

        print(f"Nome: {produto_encontrado['nome']}")
        print(f"Estoque: {produto_encontrado['estoque']}")
        print(f"Preço: R${produto_encontrado['preço']}")
        print()

        print("O que você vai editar: Nome, Estoque, Preço ? ")
        print()

        while True:

            ediçao = input("Digite aqui: ").lower()
            print()

            if ediçao == "nome":

                novo_nome = input("Digite o novo nome: ").title().strip()
                produto_encontrado["nome"] = novo_nome
                break

            elif ediçao == "estoque":

                novo_estoque = int(input("Digite o novo estoque"))
                produto_encontrado["estoque"] = novo_estoque
                break

            elif ediçao == "preço":

                novo_preço = float(input("Digite o novo preço: ").replace(",", "."))
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
            break
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
            print()

            while True:

                remover = input("Digite aqui: ")
                print()
                if remover.isnumeric():
                    remover = int(remover)
                    break
                else:
                    print("\033[33mIsso não é um número !\033[0m")

            produto_remoçao = None

            for produto in produtos:
                if produto["codigo"] == remover:
                    produto_remoçao = produto
                    break

            if produto_remoçao is not None:
                break
            else:
                print("\033[31mProduto não encontrado !\033[0m")

        produtos.remove(produto_remoçao)

        with open("produtos.json", "w", encoding="utf-8") as dados:
            json.dump(produtos, dados, ensure_ascii=False, indent=5)

        print("\033[32mProduto removido com sucesso !\033[0m")
