#Tuples -> ()
#Tuples are immutable , they cannot be changed

masala_spices = ("cardmomm" , "ginger" , "pepper")

(spice1 , spice2 , spice3 ) = masala_spices   # unpacking of the tuple

print(f"Unpacking the tuple: {spice1} , {spice2} , {spice3}")

# we can also declare the tuple directly

ratio1 , ratio2 = 4 , 9 

print(f"Ratios values: {ratio1} , {ratio2}")

# we can also flip the values

ratio1 , ratio2 = ratio2 , ratio1 

print(f"Ratios values after flipping: {ratio1} , {ratio2}")


# MEMBERSHIP CHECK

masala_spices = ("cardmomm" , "ginger" , "pepper")

print(f"Is ginger present: {'ginger' in masala_spices}")
print(f"Is ginger present: {'Ginger' in masala_spices}") # false coz case sensitive