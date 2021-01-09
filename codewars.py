
def alphabet_position(text):
    ALPHA = " abcdefghijklmnopqrstuvwxyz"
    return ''.join([str(ALPHA.index(x)) + ' ' for x in text.lower() if x.isalpha()]).strip()


def descending_order(num):
    values = [x for x in str(num)]
    values.sort(reverse=True)
    return int(values)


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])


def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

def generate_hashtag(s):
    to_return = [x.capitalize() for x in s.split()]
    print(to_return)
    return False if len(to_return) > 140 else "#" + ''.join(to_return)


def run():
    # print(str(descending_order(15)))
    # print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
    # print(alphabet_position("The sunset sets at twelve o' clock."))
    # print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
    print(generate_hashtag('Do We have A Hashtag'))


if __name__ == "__main__":
    run()
