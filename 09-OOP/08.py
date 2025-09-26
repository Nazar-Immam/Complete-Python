#Method Resolution Order (MRO)

class A:
    label = " A: Base Class"

class B(A):
    label = " B : Inherited from A"

class C(A):
    label = " C : Interited from A"

class D(B,C) :          #multiple inheritance - inherited multiple classes  
    pass

cup = D()
print(cup.label) 
#Class D does not have any label , and inherits 2 classes, from where will it take the label?
#ans - if there is common method in class , then the class inherited first gets called, like 
# here label is taken from B

#special method to know the order, (className.__mro__)
print(D.__mro__)