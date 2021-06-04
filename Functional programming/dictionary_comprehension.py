# dictionary comprehension
# these are a little bit tougher ones than list comprehension

sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

# making squares of the numbers using  dict comprehension
square_dict = {key:value**2 for key, value in sample_dict.items()}
print(square_dict)

square_dict_even = {key:value**2 for key, value in sample_dict.items() if value % 2 == 0}
print(square_dict_even)

# if you don't have a dictionary and you wanna create a dictionary of a number:number**2
square_without_dict = {num:num**2 for num in range(11)}
print(square_without_dict)

print("*" * 89)

some_list = ["a", "a", "b", "c", "d", "n", "n"]

duplicates = list({letter for letter in some_list if some_list.count(letter) > 1})

print(duplicates)
