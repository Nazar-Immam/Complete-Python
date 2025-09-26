class Chai:
    pass

print(type(Chai)) #This gives type, but Alwways remeber Everything in python is object, so , 
                  #Class is also of object type


ginger_tea = Chai()  #this is an object of class Chai

print(ginger_tea)

print(type(ginger_tea))

print(type(ginger_tea) is Chai)  #Checks if it is from class Chai , always check the type of object with class, not just object