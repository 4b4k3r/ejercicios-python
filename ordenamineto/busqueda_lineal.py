import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    
    return match


def run():
    list_size = int(input("De que tamaño es la lista: "))
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    objetivo = int(input("Cual es el objetivo: "))
    
    encontrado = (busqueda_lineal(lista, objetivo))
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

if __name__ == "__main__":
    run()