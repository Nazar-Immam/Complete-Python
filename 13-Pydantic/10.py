#Advance Nested Models Patterns/ Use cases

#Optional Nested Models
from pydantic import BaseModel
from typing import Optional, List , Union

class Address(BaseModel):
    street: str 
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None    #Nesting of a class Address,
    #optional says, address might be there or might not be, if there, then will be of Address type

class Employee(BaseModel):
    name: str
    company : Optional[Company] = None  #This is optional nesting, as employee nested company, and company
                                        #nesting  the address, so advance nesting.


#Mixed Data Types.

class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_txt: str

class Article(BaseModel):
    title: str
    sections: List[Union[ TextContent, ImageContent ]]  #Mixed Data Types.


#Deeply Nested Structures
class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country  #Nesting Country class here as data type

class City(BaseModel):
    name: str
    state: State  #Nesting State class here as a data type, and State nested Country in its fields.

class Address(BaseModel):
    name: str
    city: City    #Deeply nestesd, city here, in city it nested state, in state it nested country
    postalcode: str 

class Organization(BaseModel):
    name: str
    address : Address #again deeply nested
    branches: List[Address]=[] #empty list by default