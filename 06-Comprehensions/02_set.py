# comprehension in set  { expression(item) for item in items if condition }

favorite_chais = [
    "Masala Chai", "Ginger Tea" , "Lemon Tea" ,  
    "Lemon Tea" , "Masala Chai", "Oolong Tea"
]

# from the above lists we want only the unqiue values 
# so we'll put it in a Set by using comprehension

unique_chais = { chai for chai in favorite_chais }
print(unique_chais)

teaOnly = { tea for tea in favorite_chais if "Tea" in tea }
print(teaOnly)

#some complex example
#suppose we have a set and in that we have dictionaries (key value pairs)

recipes = {
    "Masala Chai" : [ "ginger" , "cardmom" ,"clove"] ,
    "Elaichi Chai" : [ "cardmom" ,"milk"] ,
    "Spicy Chai" : [ "ginger" , "black pepper" ,"clove"] ,
}

#we see we have a set with dictionaries and in that values are of lists

#We need to find the unqiue spices present in lists

unique_spices = { spices for ingredients in recipes.values() for spices in ingredients }

print(unique_spices)