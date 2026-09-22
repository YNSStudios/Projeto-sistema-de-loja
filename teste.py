import re

def tem_letras_e_numeros(texto):
    # Regex que valida a presença de pelo menos uma letra e um número
    padrao = r"^(?=.*[a-zA-Z])(?=.*\d)"
    return bool(re.search(padrao, str(texto)))

# Testes
print(tem_letras_e_numeros("Senha123"))  # True
print(tem_letras_e_numeros("ApenasLetras"))  # False
print(tem_letras_e_numeros("12345"))  # False


def tem_letras_e_numeros_nativo(texto):
    texto_str = str(texto)
    
    # Verifica se há pelo menos uma letra e pelo menos um número
    tem_letra = any(char.isalpha() for char in texto_str)
    tem_numero = any(char.isdigit() for char in texto_str)
    
    return tem_letra and tem_numero

# Testes
print(tem_letras_e_numeros_nativo("abc456"))  # True
print(tem_letras_e_numeros_nativo("abc"))     # False
