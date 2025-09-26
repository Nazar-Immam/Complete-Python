#add 10 percent vat at every order

def add_vat(price , rate ):
    return price + price * (rate/100)

orders = [10,20,340,400]

for i in orders :
    final = add_vat(i, 10) 
    print(f"Order value after vat : {final}")