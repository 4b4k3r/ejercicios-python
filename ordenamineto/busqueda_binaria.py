import random


def busqueda_binaria(lista, inicio, fin, objetivo):
    print(f'Buscando {objetivo} entre {lista[inicio]} y {lista[fin-1]}')
    if inicio > fin:
        return False

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, fin, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)


def run():
    list_size = int(input("De que tamaño es la lista: "))
    lista = sorted([random.randint(0, 100) for i in range(list_size)])
    print(lista)

    objetivo = int(input("Cual es el objetivo: "))

    encontrado = (busqueda_binaria(lista, 0, len(lista), objetivo))
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


if __name__ == "__main__":
    run()
