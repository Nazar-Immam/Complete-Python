# generators are same as function , except in function we use return here we use 'yield'
# It yileds one value at a time.

def chaitype() :
    yield "Cup1 : Masala Chai"
    yield "Cup2 : Ginger Chai"
    yield "Cup3 : Oolong Chai"

serve = chaitype()

for i in serve:
    print(i)


def totalcups() :
    yield "Cup1 "
    yield "Cup2 "
    yield "Cup3 "

cups = totalcups()
print(cups)
print(next(cups))
print(next(cups))
print(next(cups))
#print(next(cups)) gives stop iteration error