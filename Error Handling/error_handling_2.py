
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers! {err}")

    # if you don't wanna give the error in red
    except TypeError as err:
        print(err)
    
    # if you wanna give the same exception for 2 or more conditions
    except (TypeError, ZeroDivisionError):
        print('Hell what are you giving the input')
    else:
        print("Heyyyy")
    finally:
        print("Yoo there is another line to print is that printed?")
    print("Byeeee")
    

    

print(sum('1', 2))

