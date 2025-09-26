# walrus operator , syntax is := 
#it allows to write a statement in if conditons 

number = 13 
remainder = number % 5 

if remainder:
    print(f"Not divisible , remainder is : {remainder}")


# but by walrus ,

if ( remainder := number %5 ) :
    print(f"Not divisible , remainder is : {remainder}")


#we can also take direct inputs from user using walrus 

sizes = [ 'small' , 'large' , ' medium']

if (requested_size := input("Enter the size you want : ").lower()) in sizes :
    print(f" {requested_size} Tea getting ready")
else:
    print('Not available')


flavors = ['mint' , 'green' , 'lemon']

print("Flavors available : ", flavors)

while (flavorasked := input("Choose the flavor you want")) not in flavors :
    print("Not available ")

print(f"{flavorasked} getting ready")