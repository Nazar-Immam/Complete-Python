#LIST , List are mutable unlike tuple 
#same as array 

ingredients = [ "water" ,"tea leaves" ,"milk"]
ingredients.append("sugar")
#append always adds at the end 
#list are 0 indexed based
#so to add at any index,
ingredients.insert(1,"black tea")
print(ingredients)
ingredients.remove("water")
print(ingredients)

#to add two lists
list1 = [1,2,4,5]
list2 =[45,64,56,88,99]
list1.extend(list2)
print(list1)

last_added = list1.pop() #stores the last element in the variable, and also removes it from the list
print(last_added)
print(list1)

#to reverse a list 
list1.reverse()
print(list1)

#to sort 
list1.sort()
print(list1)

#to find min and max
max = max(list1)
min = min(list1)
print(max,min)

#in list we can also use operators like , + and * 
# + adds any two list
# * multiplies the list

#bytearray

raw_spice = bytearray(b"Cardmom")
print(raw_spice)
raw_spice = raw_spice.replace(b"Card" , b"Cinna")
print(raw_spice)