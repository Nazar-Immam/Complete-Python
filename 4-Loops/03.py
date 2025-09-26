#Enumerate()
#this is used to print numbered loop
# it returns a tuple like value, so we can give a start and value 

seasons = ["Winter" , "Summer" , "Fall" , "Spring"]

for idx, value in enumerate(seasons, start=1) :
    print(f"At {idx} : {value}")