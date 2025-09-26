#Adding validations with Field.
#Till now , we were working with BaseModel, we can also have many more models, one of them is Field.
#The Field model will help us have more and more control and ooptions on a varibale.
#there are many field parameters,
# min_length , max_length, ge(>=) , gt(greater than(>)) , le(less than equal to(<=)), lt(<), regex



from typing import Optional
from pydantic import BaseModel , Field
import re #regular expression 

class Employee(BaseModel):
    id:int 
    name: str = Field(
        ...,                #this indicates required field
        min_length=3,       #minimum length that the input should have 
        max_length=50,      #max length that the input can have 
        description="Employee Name",
        examples="Hitesh Choudhary"
    )
    department: Optional[str] = "General"  , #This means the department will take input as string, and if 
                                             # not then by default it'll take General.
    salary: float = Field(
        ...,                                 #This also means this input is cumpulsory
        ge= 10000,                          #ge is a field parameter that says, ge=greater than or equal to
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r''
    )
    #or we can also write it like this
    phone: str = Field(..., regex=r'')
    age: int = Field(
        ...,
        ge= 0,
        lt= 120 ,
        description="Age in Years",
    )
    discount: float= Field(
        ...,
        ge=0,
        le= 100,
        discription="Discount in Percentage"
    )