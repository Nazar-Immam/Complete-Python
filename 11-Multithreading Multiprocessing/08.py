#Queue in Multiprocessing.
# In processes communication is a problem, as memory is not shared and every process has its own memory
# So we need to use something which is responsible for sharing the memory - ways are - Queues , Pipes , etc
#We usually use queue for this

from multiprocessing import Process , Queue

def prepare_chai(queue):
    queue.put("Chai is ready") #In queue data strcuture, we can put any form of value, string , list , tuple , dict, any..


queue = Queue()  #This creates a queue

if __name__ == "__main__":
    p = Process(target=prepare_chai , args=(queue,))
    p.start()
    p.join()

    print(queue.get()) # by this we know, we have some data in a queue, and now any process can come and acess from here

