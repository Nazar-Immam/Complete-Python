#Dictionary
#in array we call or access a value using its index,
#but in dictionary we can name index and call value by their own name 
#many ways to initialize a dictionary

chai_oder = dict( type = "Masala Chai" , sugar = 2 , size = "large")
print(chai_oder)

#another way, common way
chai_recipie = {}
chai_recipie["base"] = "Milk"
chai_recipie['size'] = "small"
chai_recipie['sugar'] = 2

print(chai_recipie['base'])
print(chai_recipie)
#to delete, we just want to know index/key
del chai_recipie["sugar"]
print(chai_recipie)

#membership test
print('size' in chai_recipie)

#to print all the keys and values and items
print(chai_recipie.keys())
print(chai_recipie.values())
print(chai_recipie.items()) #To print both keys and values

ans = chai_recipie.get("Milk" , "Not Found")  #good way to search if not there then we can set the default value
print(ans)

#** All the things in set also works in dictionary 

#can also initialize dictionary like this
dictionary = [
    {"id" : 2},
    {"name" : 'hitesh'}
]

print(dictionary)