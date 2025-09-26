#Multi-Processing
#Threads get shared memory as they are inside Process, but Process are separate , So Processes have their OWN MEMORY.
#So when there are multiple processes(multiprocessing) then we use queue, so basically everytime in process we use queue


#In the below code , we'll check the speed of computation in threads vs process ,
#Process code takes less time, while here , the memory is getting mixed up and they are getting called simultaneously,
#so not accurate results in the below code.

#thread code
import threading
from multiprocessing import Process
import time

def heavy_cpu():
    print(f"Crunching some numbers...")
    total = 0 
    for i in range(10**7):
        total += i
    print("Done ✅")

start = time.time()

threads = [ threading.Thread(target=heavy_cpu) for i in range(2) ]
[ t.start() for t in threads]
[ t.join() for t in threads]

end = time.time()

print(f"Time Taken from Threads is: {end-start : .2f}")


#Process Code, 

startP = time.time()

if __name__ == "__main__":
    process = [ Process(target=heavy_cpu) for i in range(2)]
    [ p.start() for p in process]
    [ p.join() for p in process]

endP = time.time()

print(f"Time taken from Processes is : {endP - startP :.2f}")