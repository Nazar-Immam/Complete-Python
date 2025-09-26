#Nested Models in Pydantic

from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
    street: str 
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address     #Here we are using a reference of Address model, this is nested model.


#usage

address = Address(
    street= "329hjfa",
    city="Bhopal",
    postal_code= "343000"
)

user = User(
    id=323,
    name="Immam",
    address= address    #This is just how simply we use the nested model data
)

#There are also other ways how can we define an object or how can we pass the data
#We can put all the data in dictionary , and then pass it by unpacking

input_data = {
    "id": 232,
    "name":"Immam",
    "address": {
        "street":"325abc",
        "city" : "Bhopal",
        "postal_code":"2300099"
    }
}

user = User(**input_data)
print(user)