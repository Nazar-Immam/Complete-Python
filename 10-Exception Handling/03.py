#Catching Multiple Exceptions

def process_order(item, quantity):
    try:
        price = {"masala":20} [item] #the value is passed from arguments comes here and in this item it searches in dict
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry That chai is not on menu ")
    except ValueError:
        print("Quantity must be a number ")

process_order("masala",4)
