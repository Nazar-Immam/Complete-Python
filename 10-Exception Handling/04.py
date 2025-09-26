#Raise your own error

def brew_chai(flavor):
    if flavor not in ["masala","ginger","elaichi"]:
        raise ValueError("We don't like this chai flavor so not serving...")
    
    print(f"Brewing {flavor} chai...")

brew_chai("oolong")