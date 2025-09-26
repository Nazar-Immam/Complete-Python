#Mxing Pydantic with typing

#Some of the data types comes from Pydantic
#And some of the data types comes from typing(Built in python library) module
#by typing module, we name the datatype along with value of variables.(behaves just like in other 
#languages we define vars, ex  name: str , means name needs to be a string)

#We can also defines some datatypes using both, Pydantic & Typing

from pydantic import BaseModel
from typing import List, Dict , Optional

class Cart(BaseModel):
    user_id : int   #this ensures that the id must be an integer only
    items : List[str]     #this ensures the list will have all the string values only
    quantities : Dict[str,int] # this ensure that in the dictionary, key will be string,value will be int


class BlogPost(BaseModel):
    title: str
    content: str                                                                    
    image_url : Optional[str]=None  #Optional[x] means that the value can be of type x , if not then None.

cartdata = {
    "user_id": 32,
    "items": ["laptop" ,"Keyboard" , "mouse"],
    "quantities": { "Phones":4 , "stands":9 , "Charger":23}
}

user = Cart(**cartdata)   #we can't just pass cartdata, we need to unpack the dictionary, then pass it by**