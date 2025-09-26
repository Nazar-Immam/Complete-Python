#Deadlock Condtion.

import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("Task 1 acquired lock a ")
        with lock_b:
            print("Task 1 acquired lock b")

def task2():
    with lock_b:
        print("Task 2 acquired lcok b")
        with lock_a:
            print("Task 2 acquired lock a")

t1= threading.Thread(target=task1)
t2= threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()


#After the threads are called, both of functions executed line 1, but after that,
# they can't move, coz the lock a is aquried by task1 and lock b is acquired by task2 , 
# and no one is leaving so no one is moving therefore deadlock , fucntion will wait forever. 