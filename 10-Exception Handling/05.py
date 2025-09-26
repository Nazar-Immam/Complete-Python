#We can also create custom exceptions, Just make a class and inherit the exception class

class OutofChaiIngd(Exception):
    pass

def chai(milk , sugar):
    if milk ==0 or sugar == 0:
        raise OutofChaiIngd("Noo wayy we can't make chaii")
    print("Chai is ready ..")

chai(0,1)