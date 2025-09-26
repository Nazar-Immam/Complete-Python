#NUMBERS
#Integers

a = 11 
b = 42 
sum = a+b 
sub = b-a
print(f"Sum is: {sum}")

#Division in integers is unique
div = b/a   #gives the exact answer in decimal points
print(f"Division in python of a and b is : {div}") 

#to just get the integer value of division ,
divint = b // a
print(f"Division using // gives int value: {divint}")

#to get the Remainder of two numbers we use modulus operator
remainder = b % a 
print(f"The remainder of a and b is : {remainder}")

#to get exponential value
base = 2
power = 6
exponentvalue = base ** power 
print(f"Exponent value using ** is : {exponentvalue}")

#to write billion 
billion = 1_000_000_000 
print(billion)