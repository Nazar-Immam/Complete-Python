from pydantic import BaseModel

#Pydantic model
class Product(BaseModel):
    id: int             #|  - These are called fileds of pydantic model ,f1
    name: str           #|  - field 2
    price: float        #|  - field 3
    in_stocks: bool     #|  - field 4


product1 = Product(id=23, name="jordans", price=201050, in_stocks= True)

product2 = Product(id=12, name="courseai" ,price=4999)  #This won't give error, even though last value miss

product3 = Product(name="laptop")  #This will throw an error, coz 3 values are missing, pydantic does not
#allow to skip fields, we can only skip fields if have provided the default value in the model(class)