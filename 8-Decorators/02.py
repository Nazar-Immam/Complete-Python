
from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        print(f"Calling : {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Finished : {func.__name__}")
        return result
    return wrapper

@log_activity
def immam_result(maths, physics , Chem= 20):
    print(f"Scores: Maths : {maths} , Physics: {physics} , Chemistry: {Chem}")

immam_result(98,99)