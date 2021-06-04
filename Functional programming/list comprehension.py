# All of the possibilies that can be done with the List Comprehension

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled

doubled = [x*2 for x in vec]
# [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
greater_thatn_0 = [x for x in vec if x >= 0]
# output [0, 2, 4]

# apply a function to all the elements
positive = [abs(x) for x in vec]
#  output [4, 2, 0, 2, 4]

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fruits_nospaces = [weapon.strip() for weapon in freshfruit]
# output ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
squares = [(x, x**2) for x in range(6)]
# output [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
unpacking_tuple = [num for elem in vec for num in elem]
# output [1, 2, 3, 4, 5, 6, 7, 8, 9]