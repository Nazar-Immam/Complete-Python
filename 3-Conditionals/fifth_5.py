#when we usually take input, it takes string by defualt
#we can alter it by wrapping

amount = int(input("Enter the amount :"))

# print(f"Data type of amount : {type(amount)}")

# if amount > 300 :
#     print("Free Delivery")
# else:
#     print("Not free delivery")    


# Terniary 

deliveryfees = 0 if amount>300 else 30
print(deliveryfees)