# Decorators are made to wrap some function, we make a decorator and pass function as an argument
#Once decorator is made then we just use its name with @ and on above of any function we can write and it would 
# act as the decorator of that function 

from functools import wraps       #this preserves the names of the function and other meta data

def my_decorator( func ):
    @wraps(func)
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def greet():
    print("Hey this is function call with decorator from greet")

greet()

print(greet.__name__)