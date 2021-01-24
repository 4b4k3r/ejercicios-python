
def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


def run():
    palabra = input("Escribe un palabra: ")
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()
