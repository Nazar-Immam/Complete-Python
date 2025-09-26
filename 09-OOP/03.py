#Attribute Shadowing

#When a variable initialised inside class , they are called attributes.

class Chai():
    temperature = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.temperature)
cutting.temperature = "mild"
print(cutting.temperature)
del cutting.temperature
print(cutting.temperature)

#this shows,if we assinged some value to an attribute of an object, and then delete that attribute value, 
#and print,then it would still print the value without error,by taking the value from the class as a fallback.
#This is called attribute shadowing, if we didn't had value in original class then it would give error, 
#But here it fallbacks to the like shadow.