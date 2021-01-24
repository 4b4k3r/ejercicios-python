from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

x_once = []
y_once = []


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_cordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        a = campo.coordenadas_de_borrachos[borracho].x
        b = campo.coordenadas_de_borrachos[borracho].y
        x_once.append(a)
        y_once.append(b)

    return inicio.distancia(campo.obtener_cordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipp_de_borracho):
    borracho = tipp_de_borracho(nombre='Joel')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='Distancia media')
    show(grafica)


def caminata_borracho(distancias_de_caminata, numero_de_intentos, tipp_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipp_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipp_de_borracho.__name__} tuvo una caminata aleatoria de {pasos} pasos con distancia media de {distancia_media}, distancia maxima de {distancia_maxima} y distancia minima de {distancia_minima}')
    graficar(x_once, y_once)


if __name__ == '__main__':
    distancias_de_caminata = [100000]
    numero_de_intentos = 1
    caminata_borracho(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
