import random


def generar_contrasena():
    MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    MINUSCULAS = "abcdefghijlmnopqrstuvwxyz"
    NUMEROS = '0123456789'
    SIMBOLOS = '!@#$%^&*)(_-+='

    caracteres = MAYUSCULAS + MINUSCULAS + NUMEROS + SIMBOLOS
    contrasena = []

    for i in range(0,15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    return "".join(contrasena)


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == "__main__":
    run()
