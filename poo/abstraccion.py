
class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self.llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    
    def llenar_tanque_de_agua(self, temperatura):
        print(f'llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()