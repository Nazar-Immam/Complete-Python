#Comprehension in generator
#Generators are used for saving memory
#comprehension in generator uses exact same syntax, just it uses parenthesis ()
#Syntax -  ( expression for item in items if condtion )

# difference, like both works the same just ,
#1. [ x for x in items ]              -- This makes entire list in memory
#2. ( x for x in items )              -- This takes one by one input and stores one by one like a stream   

dailsales = [ 23,5,57,8,5,43,2,3,2,2,2]

# sum the total sales above 5 
#generators provides in built funcitons like filter sum directly on the comprehension

total = sum( sales for sales in dailsales if sales > 5)
print(total)