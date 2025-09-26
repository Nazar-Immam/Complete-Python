#Inheritance and Composition in Python

#Inheritance - If one class has done some work , then we can inherit that class, in programming we can inherit any class

class BaseChai:

    def __init__(self, type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing {self.type_}....")


#To inherit the class we use parenthesis and then pass the class name that we want to inherit

class MasalaChai(BaseChai):

    def add_spices(self):
        print(f"Adding Cardmom , ginger , cloves")


#Conmposition - In this we don'nt make object of a class, we just take all the properties of a
#class in another class with a varibale

class ChaiShop:
    chai_cls = BaseChai  #here we are taking all properties of basechai class, but not making an object of it.

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type_} chai in the shop")
        self.chai.prepare()



class FancyChaiShop(ChaiShop):   #Inheritance
    chai_cls = MasalaChai        #Composition


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()