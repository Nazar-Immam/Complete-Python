#Pydantic Serialization
#Serialization- It is a way of converting complex data structures into readable formats.
#In Pydantic Serialization,
#Pydantic Models are converted into readable formats , like Python Dictionary, or JSON string, or XML

#Two primary methods for serialization:
#1 obj.model_dump(): This method converts the model into a standard Python dictionary. 
#This is useful for internal application logic.
#2 obj.model_dump_json(): This method serializes the model directly into a JSON-encoded string,
#which is ideal for transmitting data over a network, such as in an API response.

from pydantic import BaseModel , ConfigDict #(used to configure pydantic models into dictionaries)
from typing import List 
from datetime import datetime

class Address(BaseModel):
    city: str
    street: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str 
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    #datetime mostly is not compatible with pydantic models,so we need to customize it using confidict
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')} #strftime(stringformattedtime)
        #very important always do this (lamda function with datetime, strftime...)
    )

#usage

user = User(
    id=1,
    name="Immam",
    email="ajfd@mail.com",
    is_active=True,
    createdAt=datetime(2025,9,25,22,48,15),
    address= Address(
        city="Jabalpur",
        street="Civil Lines",
        zip_code="329000"
    ),
    tags=["Premium User", "Commercial User"]
)

python_dict = user.model_dump()  #Converts the model into python dictionary
print(python_dict)

print("= "*50)

json_str = user.model_dump_json()  #Converts Everythin Into JSON string
print(json_str)