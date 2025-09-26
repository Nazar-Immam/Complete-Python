#working with pydantic, always
# import BaseModel
# Give Type annotations(like, int , str, bool , etc)
# Model init( Always use the unpack dictionary, (**var))
# Automatic Data Validation - Pydantic always tries to change the datatype to fit it correctly, if it is 
# unable to do that, then it raises an error message



from pydantic import BaseModel

#this class is called defining pydantic model,
class User(BaseModel):
    id : int
    name: str
    is_active: bool


inputdata = {"id": 12 , "name": "Immam" , "is_active": True}

obj = User(**inputdata) #This will unpack the dictionary.
print(obj)