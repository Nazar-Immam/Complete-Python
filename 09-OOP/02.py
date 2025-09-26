#NameSpaces = Each object possess its own identity and its own features, though being from the same class
#Any variable inside class is called properties

class Chai:
    origin = "India"

print(Chai.origin)  # We can access the properties of class using dot operator

#we can also declare variables in class from outside using dot operator

Chai.is_true = "True"

print(Chai.is_true)

#Creating objects from class Chai
masala = Chai()  #object
print(masala.origin)
print(masala.is_true)

#Now changing the properties
masala.origin = "Nepal"

print(Chai.origin)   #This shows changing the object value doesnt affects the class values
print(masala.origin) #This shows that every object can have value of its own.

#We can also add new properties to objects. like,
masala.flavor = "Spicy"
print(masala.flavor)