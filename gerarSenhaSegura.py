tamanhoSenha = int(input("Digite o tamanho da senha desejada: "))
import random
import string

def gerar_senha(tamanho):
    if tamanho < 8:
        raise ValueError("O tamanho da senha deve ser no mínimo 8 para garantir a inclusão de todos os tipos de caracteres.")

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(digitos),
        random.choice(simbolos)
    ]

    todos_caracteres = letras_maiusculas + letras_minusculas + digitos + simbolos
    senha += random.choices(todos_caracteres, k=tamanho - 4)

    random.shuffle(senha)

    return ''.join(senha)

senha_gerada = gerar_senha(tamanhoSenha)

if senha_gerada:
    print("Senha gerada com sucesso:", senha_gerada)
