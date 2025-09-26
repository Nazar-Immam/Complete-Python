
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} Chai")
        if flavor == "unknown":
            raise ValueError("Unavilable !")
        
    except ValueError as e:   #we can call valueeror as e here or anything we want
        print("Error :" , e)
    else:  #this else if of (try except)-else part, not if else
        print(f"{flavor} Chai is served ")
    finally:   #finally runs everytime no matter what
        print("Next Order Please ! ")


serve_chai("Masala")
serve_chai("unknown")
