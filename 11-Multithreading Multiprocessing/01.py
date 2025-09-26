#Multithreading ( Threading Module ) [ CONCURRENCY]

import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order {i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for order {i}")
        time.sleep(3)

# take_orders()
# brew_chai()
#The above methods, would just complete one function and then move to second , but we want that 
#These functions gets called simultaneously, so in order to do that we need to execute those function simultaneously, 
#so we need to use thread for that

#Creating Threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

#Now start the thread
order_thread.start()
brew_thread.start()

#now since thread can have sleep time, or slow speed,we want out main program to wait for the thread completion and
# then move on, so we use join() method, that waits until thread finishes

order_thread.join()
brew_thread.join()

print("All orders taken and served !")

#THE ABOVE EX WAS OF MULTITHREADING(CONCURRENCY), - HERE WE HAVE ONLY ONE CORE OF THE CPU WORKING, 
#AND IN THAT ONE CORE THE PROCESS KEEPS SWTICHING BETWEEN MULTTIPLE THREADS, SO MULTITHREADING
