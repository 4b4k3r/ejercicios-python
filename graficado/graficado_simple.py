from bokeh.plotting import figure, output_file, show


def run():
    output_file('graficado_simple.html')
    fig = figure()

    total_valores = int(input("Cuantos valores quieres graficar: "))
    x_values = list(range(total_valores))
    y_vals = []

    for i in x_values:
        val = int(input(f"valor \"Y\" para {i}: "))
        y_vals.append(val)

    fig.line(x_values, y_vals, line_width=2)
    show(fig)

if __name__ == "__main__":
    run()
