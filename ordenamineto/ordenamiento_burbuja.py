import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)
    pasos = 1

    for i in range(n):
        for j in range(0, n - i - 1):
            print(pasos)
            pasos += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


def run():
    list_size = int(input("De que tamaño es la lista: "))
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)
    print(ordenamiento_de_burbuja(lista))

if __name__ == "__main__":
    run()