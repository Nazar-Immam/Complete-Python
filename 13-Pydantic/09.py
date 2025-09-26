#Self Referencing / Recursive Models in Pydantic

#Ex- We comment on something, and someone comments on our comment as a reply,
#and on that reply someone again commented and it goes on and on ...

from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None
    #this says, that replies are optional, they might or might not be present,
    #if present then they are of type List and List of type 'Comment' (which itself is a pydantic model)
    #and everthing aside, the default value is None.

#when ever we are self refrencing any model, always use, modelname.model_rebuild()
Comment.model_rebuild()  #forward referencing. required to do self referencing

#usage

comment = Comment(
    id=1,
    content="First Comment",
    replies= [
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2"),
        Comment(id=4, content="reply 3", replies= [
            Comment(id=41, content="repy1 on reply3"),
            Comment(id=42, content="repy2 on reply3"),
        ]),
    ]
)

print(comment)