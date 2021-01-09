import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Ingresa un numero del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Elige un numero mas grande")
        else:
            print("Elige un numero mas chico")

        numero_elegido = int(input("Elige otro numero: "))

    print("GANASTE")


if __name__ == "__main__":
    run()