#Documenting your code.
# when we write our any function , just at the start of the fucntion we write in tripple qoutes shows at the console
# """anything"""   = By doing this , we get alot of builtin functions, 
# like showing the name of the function which helps in debugging.
# dunder doc  - __doc__

def chai(flavor):
    """ Return the flavor of the Chai """
    return flavor

print(chai.__doc__)
print(chai.__name__)