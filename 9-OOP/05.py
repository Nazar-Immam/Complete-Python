#Constructors and init in python
#Constructors are a type of method , it is used when , when we want that whenever an object is created,
# it by defualt has some properties and that we make it in constructors
#to make constructors there is a reserved keyword that is used called - __init__
#so __init__ is used to build constructors

class ChaiOrder:
    
    def __init__(self , type_ , size):  #we used type_ becoz type is a keyword so we cannot use that , 
        self.type_ = type_
        self.size = size

    def describe(self):
        return f"{self.size} ml of {self.type_} chai"


order = ChaiOrder("Masala" , 200)
print(order.describe())

order2 = ChaiOrder("Ginger" , 150)
print(order2.describe())