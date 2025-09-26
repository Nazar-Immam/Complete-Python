#Advance Validations in Python. / Use cases of Validations

from pydantic import BaseModel, field_validator , model_validator
import datetime

class Person(BaseModel):
    first_name: str 
    last_name: str 

    #we can pass multiple fields in field validators
    #this is known as multiple field validation
    @field_validator('first_name','last_name')
    def captialname(cls,v):
        if not v.istitle(): # value.istitle() checks for captial letters 
            raise ValueError("Names must be capitalized")
        return v 


#Data Transformations Patterns 

class User(BaseModel):
    email: str 

    @field_validator('email')
    def normalize(cls,v):
        return v.lower().strip()   #Makes all the letters in lowercase and by strip removes extra spaces
    


#Some times we need that field validations run before the model itself,
#this is how we do that (mode='before') helps us in that
class Product(BaseModel):
    price:str #$4.45

    @field_validator('price',mode='before') #By mode='before', this field is checked before the model runs
    def parse_price(cls,v):
        if isinstance(v,str):   #Checks if the varibale v is a string or not
            return float(v.replace('$',''))  #changes it to float,and replaces '$' with nothing
        return v
    


#Model Validation

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='before')
    def validate_date_range(cls,values):
        if values.start_date >= values.end_date:
            raise ValueError("End date should only be after start date")
        return values
    
