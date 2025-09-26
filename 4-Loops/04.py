#zip
#to run loops simultaneously from different lists

names = ["Hitesh" , "Carlos" , "John" , "Piyush"]
amount = ["10","15","11","20"]

#we need to print every name with its amount simultaneously
#we use zip and pass both the list and it returns tuple at every iteration

for names, amount in zip(names,amount):
    print(f"{names} paid : {amount}")