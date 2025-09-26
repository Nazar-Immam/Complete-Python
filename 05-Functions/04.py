#to access variables in just above function in latest function we use 'nonlocal' keyword

def chai():
    chai_type = "Oolong"
    def kitchen():
        nonlocal chai_type    #accessed the above function variable inside a function 
        chai_type = "Ginger"   #this changes the outside varibale 
        print(chai_type)
    kitchen()

chai()

#to access the global variable, use keyword 'global'

name = "Hitesh"

def change():
    global name 
    name = "Immam"
    print(name)
    
change()

print(name) #changes the global variable

#Always avoid using global variables , coz if it gets changed , it would disturb many other functions