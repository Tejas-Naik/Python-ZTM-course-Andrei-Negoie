from functools import reduce        # we have to import reduce as it is not default imported

# reduce function

my_list = [1, 2, 3]


def accumulator(acc, item):     # acc = initializer
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 2))
