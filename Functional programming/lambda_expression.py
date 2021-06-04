my_list = range(101)

print(list(map(lambda item: item**2, my_list)))
print(list(filter(lambda item: item % 2 == 1, my_list)))
print(list(map(lambda item: item**2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])

print(a)

# docs lambda function
# the lambda function can be used as a function inside a function like the following


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(12)
print(f(3))
print(f(13))

# you can use lambda as a key for sort or anything else
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
# what if you wanna sort the list by the second argument
pairs.sort(key=lambda x: x[1])
print(pairs)


