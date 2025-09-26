#3 ways to access base class in inheritance


class Chai:
    def __init__(self, type_ , strength):
        self.type_ = type_
        self.strength = strength


#.1 Code Duplication
class GingerChai(Chai):
    def __init__(self,type_,strength , spice_level):
        self.type_ = type_
        self.strength = strength
        self.spice_level = spice_level



#.2 Explicit Call
class MasalaChai(Chai):
    def __init__(self,type_,strength, spice_level):
        Chai.__init__(self,type_,strength)
        self.spice_level = spice_level


#.3 super()  -- this one is used widely
class AdrakChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level