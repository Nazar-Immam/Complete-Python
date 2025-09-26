#Thread ex.
#Imp,
#In a Process, there are multiple threads, and by threading we just control one or two threads which 
#is inside the main process, we should remeber that thread works with only one core cpu. unlike process,

import threading
import time

def preparechai(type_ , wait_time):
    print(f"{type_} Chai status: Brewing... ")
    time.sleep(wait_time)
    print(f"{type_} Chai is Ready !")


t1 = threading.Thread(target=preparechai , args=("Masala",2))  #in thread & process args always takes tuple 
           #input,if we want to pass just one input then we need to write comma(,) after it, like args=(21,)
t2 = threading.Thread(target=preparechai , args=("Ginger",3))

t1.start()
t2.start()

t1.join()
t2.join()