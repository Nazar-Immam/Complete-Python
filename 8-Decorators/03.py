from functools import wraps

def authorization(func):
    @wraps(func)
    def wrapper(user):
        print(f"Calling {func.__name__}")

        if user != "admin":
            print("Access Denied !")
            return None
        else:
            return func(user)
        
    return wrapper
        

@authorization
def authentication(name):
    print("Access granted to Tea Inventory")

authentication("ghost")

authentication("admin")