# filter is just filters things

my_list = [1, 2, 3, 4, 5, 6, 7]


def only_odd(item):
    return item % 2 == 1


print(list(filter(only_odd, my_list)))

