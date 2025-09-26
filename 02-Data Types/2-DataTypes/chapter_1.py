sugar_quantitiy = 2
print(f"The quantity of sugar is {sugar_quantitiy}")

sugar_quantitiy = 12
print(f"The quantity of sugar now is {sugar_quantitiy}")

#Everything in Python is treated as object
# Object has three properties= Identity , type , value

#To check the mutability or immutability of a variable always check from identity and never from value

#To find identity , 
print(id(2))
print(id(12)) #we see that even though values of sugar quantity has changed from 2 to 12 but identity is different
#therefore number is immutable.
#What happens is the reference variable remains same but in memory new space get allocated for value and now 
#reference variable points to the new value.