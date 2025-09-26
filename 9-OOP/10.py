#Classmethod 
class Chaiorder:

    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    #Classmethod - We want a constructor that can accept values like dictionary, lists etc apart from direct values
    #So we use classmethod for that
    # In this we don't write self , we write cls, and above that, @classmethod decorator

    @classmethod
    def from_dict(cls , order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type , sweetness , size = order_string.split(",")
        return cls(tea_type,sweetness,size)
    

order1 = Chaiorder.from_dict({"tea_type": "masala", "sweetness":"low" , "size": "large"})

order2 = Chaiorder.from_string("Ginger,Low,Small")

print(order1.__dict__)
print(order2.__dict__)