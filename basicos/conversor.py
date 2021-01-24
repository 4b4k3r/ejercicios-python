def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?:")
    pesos = float(pesos)
    dolares = str(round((pesos / valor_dolar), 2))
    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 💰

1.- Pesos Colombianos
2.- Pesos Argentinos
3.- Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))


if opcion == 1:
    conversor("colombianos", 3875)
elif opcion ==2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta")


