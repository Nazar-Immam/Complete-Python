#Syntax  [ expression for i in items if condition ]

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

#we need to take out all the iced tea

iced_tea = [tea for tea in menu if "Iced" in tea ]
print(iced_tea)

length = [ lt for lt in menu if len(lt) < 12]
print(length)

