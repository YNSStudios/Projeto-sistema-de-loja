import json
from time import sleep

print("[1] Login")
print("[2] Cadastrar")

while True:

    escolha = input()
    if escolha.isnumeric():
        break
    else:
        print("\033[31mIsso não é um número !\033[0m")

