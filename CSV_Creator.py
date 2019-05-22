import random


def get_random_char():
    # get random int from the interval of char '0' number from the ASCII table
    # to 'z'
    ranodom_symbol_num = random.randint(ord('0'), ord('z'))
    return chr(ranodom_symbol_num)


csv_list = []
for i in range(1000):
    hash_string = ''
    for _ in range(16):
        hash_string += get_random_char()

    csv_list.append((i + 1, hash_string))
