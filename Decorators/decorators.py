
# the syntax of Decorators is they have @name_of_decorator

# @classmethod
# @staticmethod

def hello():
    print('Hello')


greet = hello()
del hello

print(greet)


# functions in Python are the First Class Citizen
# they act as the Variables

def hello(func):
    func()


def greet():
    print("Helloooo")


print(hello(greet))

# TIP:  Decorators Supercharge our functions

# Higher Order Function
# Higher order function is a function that accepts a function as a Parameter
# or a function that returns another function ex.map(), filter(), reduce()


# our first decorator
print("Decorators (****************************************)")


def my_decorator(func):
    def wrap():
        print("********")
        func()
        print("********")
    return wrap


@my_decorator
def add_decorator():
    print("Helllooo")


add_decorator()

print("Decorators (********************input********************)")


def my_decorator(func):
    def wrap(x):
        print("********")
        func(x)
        print("********")
    return wrap


@my_decorator
def add_decorator(greet):
    print(greet)


add_decorator('hii')

print("*******************Easy trick*******************")

def my_decorator(func):
    def wrap(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")
    return wrap


@my_decorator
def add_decorator(greet, emoji='😁😁'):
    print(greet, emoji)


add_decorator('hii')

