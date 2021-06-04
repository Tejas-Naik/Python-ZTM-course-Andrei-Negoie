# zip function zips to iterables together like lists
my_list = [1, 2, 3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))

names = ["Tim", "Andrei", "Jonas", "Colt", "Angela"]
students = [1200000, 500000, 850000, 800000, 790000]
courses = [19, 25, 5, 7, 5]

print(list(zip(names, students, courses)))

