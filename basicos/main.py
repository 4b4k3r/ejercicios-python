import re


def order(sentence):
    words = []
    for i in range(1, len(sentence.split()) + 1):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
                break

    return " ".join(words)


def iq_test(numbers):
    odd = [car for car in numbers.split() if int(car) % 2 == 0]
    even = [car for car in numbers.split() if int(car) % 2 != 0]
    return numbers.split().index(even[0]) + 1 if len(odd) > len(even) else numbers.split().index(odd[0]) + 1


def unique_in_order(iterable):
    last = ''
    to_return = []

    for x in iterable:
        if last != x and last != '':
            to_return.append(last)
        last = x
    if last != '':
        to_return.append(last)

    return to_return


def run():
    # Use a breakpoint in the code line below to debug your script.
    # print(unique_in_order('AAAABBBCCDAABBB'))
    # print(iq_test("43 28 1 91"))
    print(order("is2 Thi1s T4est 3a"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
