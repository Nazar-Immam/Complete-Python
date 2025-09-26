
def makechai(milk , sugar , chai):
    print(milk,sugar, chai)

#Passing of arguments

makechai("yes" , "no" , "Darjeeling")  #agrs  #positional
makechai(chai= "Darjeeling" , sugar="yes" , milk= "Yes")  #kwargs , keywords arguments


#We can also have both ways , 
# in Parameters we can write *anyname , **anyword . 
#in this, one astrik takes all the named agruments and double astrik handels all the unnamed arguments or keyword args

def argsStudy( *anything , **extras) :
    print(anything)
    print(extras)

argsStudy("Hitesh", "12" , 8 , num=12 , name="Immam" , place="Bhopal")


#To return multiple values

def amount():
    return 20 , 200 ,30

a , b , _= amount()

print(a)
print(b)