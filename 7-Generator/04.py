#Yield from( yield value from different functions/generators) and Close the Generators

def local_chai():
    yield "Masala Chai "
    yield "Ginger Chai "

def imported_chai():
    yield "Matcha Chai"
    yield "Oolong Chai"


def menu():
    yield from local_chai()
    yield from imported_chai()

for i in menu():
    print(i)


# how to close generator

def chai_stall():
    try:
        while True:
            order = yield "Wating for the order !"
    except:
        print("Stall Closed !")

stall = chai_stall()
print(next(stall)) # Starts the generator 

stall.close() #closes the generator , and cleans up the memory, Very necessary . Must doo