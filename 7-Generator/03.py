# Send value to generators

def chai_customer() :
    print("Welcome, what would you like to order ?")
    order = yield 
    while True:
        print(f"Preparing {order}")
        order = yield

stall = chai_customer()
next(stall)  #This starts the generator
#Send value to the generator using .send()
stall.send("Masala Chai")
stall.send("Ginger Chai ")

