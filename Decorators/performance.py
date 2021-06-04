# we are gonna build a function that calculates the time took bu the function provided to it
from time import time
import random


def performance(func):
    
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"The time tool to run this function is {end_time - start_time}s")
        return result
    return wrapper
    


@performance
def calculate():
    for i in range(10):
        i * 100

calculate()


