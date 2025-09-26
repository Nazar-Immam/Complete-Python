#Threads example

import threading
import time

def boiling_milk():
    print("Boiling Milk...")
    time.sleep(2)
    print("Milk Boiled")

def toast_bun():
    print("Toasting Bun...")
    time.sleep(2)
    print("Bun toasted..")

# toast_bun()    | -we can call the function normally, but threading allows us to set which part executes which function
# boiling_milk() | -In general threading gives more control to us , also enhances speed of execution

start = time.time()

t1 = threading.Thread(target=boiling_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Time taken is: {end - start:.2f}")