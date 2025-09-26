#MULTIPROCESSING( multiprocessing.process module) [ PARALLELISM ] 
#Here multiple cores are doing multiple tasks(processes) , its like 3 tasks are done by 3 workers at the same time.
#Each process has its own memory unlike threads(they share memory)

from multiprocessing import Process
import time 

def brew_chai(name):
    print(f"Start of {name} chai brewing ")
    time.sleep(3)
    print(f"End of {name} chai brewing ")


if __name__ =="__main__":      #always make process inside this block only,
    chai_makers = [            #This is just a list comprehension, we can make process using a variable also
        Process(target=brew_chai , args = (f"Chai Maker {i+1}",))
        for i in range(3)
    ]

    #start all processes
    for p in chai_makers:
        p.start()

    #wait for all the process to complete
    for p in chai_makers:
        p.join()
    
    print("All Chai Served")



# Simple way of creating a process
# if __name__ == "__main__":
#     p = Process(target= function_name , args =(agruments to that function,))
#     p.start()
#     p.join()

#We can also make a process, just with p = Process(taget=function name),
#without passsing args, and also we can pass many other function also ..