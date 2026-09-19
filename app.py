import json
import random 
from time import sleep

try:
    with open('produtos.josn', 'r', encoding='utf-8') as dados:
        produtos = json.load(dados)

except FileNotFoundError:
    produtos = []

