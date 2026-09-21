import json
from time import sleep

try:
    with open("clientes.json", 'r', encoding="utf-8") as dados:
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

    escolha = input()
    if escolha.isnumeric():
        break
    else:
        print("\033[31mIsso não é um número !\033[0m")