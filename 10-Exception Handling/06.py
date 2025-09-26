class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = { "masala": 20 , "ginger":50 }
    try:
        if flavor not in menu:
            raise InvalidChaiError("Not giving for now")
        if not isinstance(cups, int):  # isinsatance() checks if the value is int , float , or any datatype
            raise TypeError("Value should be an integer")
        
        total = menu[flavor] * cups

        print(f"Your Bill for {cups} cups of {flavor} chai is: {total} ")

    except Exception as e:
        print("Error",e)
    
    finally:
        print("Thank you for visiting !")


bill("mint",3)
bill("masala","Three")
bill("ginger",4)