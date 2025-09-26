#Field and Model Validators in python

from pydantic import BaseModel, field_validator , model_validator

#not everything is possible with fields, so we use field_validator to make our custom field validations

#Field validator
class User(BaseModel):
    username: str


    @field_validator('username')  #in this we pass the field that we need to have custom validation for
    def username_length(cls,v):    #v is the value here, the data/input came.
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return v   #This is very important to return the value irrespective of anything



#We also have MODEL VALIDATORS, THAT VALIDATES THE ENTIRE MODEL
#And they can access multiple fields simultaneously also.

#Model validators

class SignUpdata(BaseModel):
    password: str 
    confirm_password: str

    @model_validator(mode='after') #This mode 'after' executes this model validator after every other thing
    def pass_match(cls, values):   #Since this is a model validator, values contains every value of model
        if values.passwaord != values.confirm_password :
            raise ValueError("Password didn't matched.")
        return values   #This is very important to return all the values irrespective of anything