#Computed Property in Pydantic
#A computed property in Pydantic = a field that is calculated automatically
#from other fields, not provided by the user.

from pydantic import BaseModel , computed_field, Field

class Product(BaseModel):
    price: float
    quantity : int 

    #now we want to calculate the total price of it, we can have other variables,
    #but in pydanctic we can calculate here only with new field, using computed-field

    @computed_field #- this marks the field as computed, that means the field will be computated when called
    @property       #- this makes the field accessible as the attribute, just like other fields
    def totat_price(self) -> float:
        return self.price * self.quantity
    
#we have a function , model_dump() , this shows whatever is in the model, this is used with the object
user = Product(
    price=500,
    quantity=13
)

print(user.model_dump) #In this we see, even though we didn't have the total price field, but it is present
    

class Booking(BaseModel):
    user_id: int 
    room_id: int 
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def totalbill(self)->float:
        return self.rate_per_night * self.nights
    
book = Booking(
    user_id=2,
    room_id=32,
    nights=4,
    rate_per_night=25.5
)

print(book.model_dump)
print(book.totalbill)   #we can access the computated propertly like this, coz we added @property 
