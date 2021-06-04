# set comprehensions are same as List comprehensions but the difference is we use
# {} instead of [] 

my_set = {char for char in "hello"}
print(my_set)

num_100 = {num for num in range(1, 101)}
print(num_100)

square_set = {num**2 for num in range(11)}     # makes the square of the number
print(square_set)

square_set_even = {num**2 for num in range(11) if num % 2 == 0}
