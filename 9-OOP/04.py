#Self Argument in python.
#When functions are created inside Class they are called as 'methods'

class Chaicup:
    size = 150 

    def describe(self):  #The self keyword allows to access all the varibles and attributes of class inside function
        return f"The chai is of {self.size} ml"  #To access the variables outside class we use self with dot operator
    

chai = Chaicup()
print(chai.describe())
  
print(Chaicup.describe(chai))  #While calling from the method from direct class , we need to pass object name

chai2 = Chaicup()
chai2.size = 300
print(chai2.describe())
print(Chaicup.describe(chai2))

    