import re


def rot13(message):
    dic = 'abcdefghijklmnopqrstuvwxyz'
    values = []
    for x in message:
        if not x.isalpha():
            values.append(x)
            continue

        dic = dic.lower() if x.islower() else dic.upper()
        values.append(
            dic[dic.index(x)-13: None if dic.index(x)-12 == 0 else dic.index(x)-12])

    return ''.join(values)


def increment_string(strng):
    number = strng.replace(re.sub('([0-9])+$', '', strng), '')
    return ''.join([strng.replace(number, ''), str(int('0' if number == '' else number) + 1).zfill(len(number))])


def solution(args):
    values = []
    last = None
    range_in = []
    for number in args:
        if last is None:
            last = number
            continue

        range_in.append(last)

        if (last + 1) != number:
            if len(range_in) > 2:
                values.append(outer(range_in))
            else:
                values.append(','.join(map(str,range_in)))
            
            range_in = []
            last = None

        last = number

    range_in.append(last)
    if (last + 1) != number:
        values.append(values.append(outer(range_in)) if len(range_in) > 2 else '')
        values.append(','.join(map(str,range_in)) if len(range_in) < 3 else '')

    return ','.join(values)

def my_func():
    respuesta = 0
    values = []
    for i in range(2000):
        values.append(i)
        respuesta += 1

    print(values)
    return respuesta


def outer(range_in):
    return ''.join(str(range_in[0])) + '-' + ''.join(map(str,range_in[len(range_in)-1:]))


def mix(s1, s2):
    pass

def run():
    # print(increment_string("foobar009"))
    # print(rot13("mM"))
    # print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
    # print(mix("Are they here", "yes, they are here"))
    print(my_func())


if __name__ == "__main__":
    run()
