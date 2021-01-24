
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre=nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')


def solve(arr):
    return [sum([1 for x in range(len(y)) if ((ord(y[x])) - 97) == x]) for y in arr]


def main():
    print(solve(["abode", "ABc", "xyzD"]))
    # persona = Persona('Joel')
    # persona.avanza()

    # ciclista = Ciclista('Daniel')
    # ciclista.avanza()


if __name__ == "__main__":
    main()
