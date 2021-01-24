
def narcissistic(value):
    sum_val = 0
    length = len(str(value))

    for car in str(value):
        increment_value = int(car)**length
        sum_val += increment_value

    return sum_val == value


def run():
    print(str(narcissistic(int(input("Ingrese un valor: ")))))


if __name__ == "__main__":
    run()
