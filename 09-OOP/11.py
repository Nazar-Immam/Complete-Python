#Property decorator - getter setter
#The properties(variables) in a class are and can be controlled by anyone outside of it.
#They can be accessed , modified and changed, but we dont want this everytime or for some variables.
#So to not give control of variables, we have a certain way of defining those.

class TeaLeaf:
    def __init__(self, age):
        self._age = age     #when we assign variable with underscore then it is assumed that it is special,
     #and must have some ways to acess that, and python treats _age as age only, it neglects the underscore

    
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self,age):
        if 1<= age <=5 :
            self._age = age
        else:
            raise ValueError("Age must be between 1 and 5")
    
leaf = TeaLeaf(2) # we passing 2 but its getting 4 by +2 , so we again controlling the variable, this is what @property Dec. does
print(leaf.age)
leaf.age = 5 #after setting more than 5 it is giving error, so we are controlling the variable
print(leaf.age)