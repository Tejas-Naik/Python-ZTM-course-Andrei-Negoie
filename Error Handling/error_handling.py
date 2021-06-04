# taking input from the user 
try:
    age = int(input("Please enter your age: "))
    print(age)
except:
    print("please enter a number instead! ")
    print('bye')


# if you wanna ask their age until they enter the correct number use While Loop
while True:
    try:
        age = int(input("Please enter your age: "))
        print(age)
    except:
        print("please enter a number instead! ")
    else:
        break

