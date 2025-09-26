#STRING
#Strings are IMMUTABLE in python , just like in java

name = "Immam"
want = "Knowledge"

print(f" Please serve {want} for {name}")

#Indexing starts from 0
#Last number is not inclusive, like 6 letter string, then we need to write 0 to 7 to print

#Slicing
chainame = "Aromatic and Bold"
print(f"Choosen Word : {chainame[5]}")
print(f"Choosen Word : {chainame[0:5]}")
print(f"Choosen Word : {chainame[12:]}") #This gives the start point and till end
# in indexing we can also use step. = Slicing
# [start: end : step] // step means how many after each repititions to print ex
print(f"Print this : {chainame[0:15:3]}") #This prints every 3rd letter

#WE CAN USE THIS TO REVERSE A STRING
print(f"Reverse of string : {chainame[::-1]}") #if we dont write start and end it by default accepts it as start end


#ENCODED STRING , sometimes when we use special characters of different langs , then we use this to make it normal
label_text = "Chai Special" 
encoded_label = label_text.encode("utf-8")
print(label_text)
#once you encode you also need to decode
decoded_label = encoded_label.decode("utf-8")