# for the map function we give a function (action to act), a data action to act on that data.

def multiply_by2(li):
    new_list = []
    for number in li:
        new_list.append(number*2)
    return new_list


print(multiply_by2([1, 2, 3]))


# using map function
def multiply_by_2(item):
    return item*2


print(list(map(multiply_by_2, [1, 2, 3])))

# function that returns usernames in all uppercase letters.
usernames = ["RN_Tejas", "RN_Tejasprogrammer", "Rajendra Naik", "yooo", "Brainnnni", "Ouuuuut"]


def no_lower(item):
    return item.upper()


print(list(map(no_lower, usernames)))

# squares function
list_squares = list(range(1, 101))
print(list_squares)


def square(number):
    return number**2


square_list = list(map(square, list_squares))


def square_root(number):
    return number // number


print(list(map(square_root, square_list)))


def no_upper(string):
    return string.lower()


print(list(map(no_upper, 'TEJAS')))