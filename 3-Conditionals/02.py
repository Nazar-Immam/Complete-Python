#to take input just write input

snack = input("Enter your preffered snack: ").lower()  #this makes the readability easy , as bUrgEr will read as burger

print(f"User asked for: {snack}")

if snack == "samosa" or snack == "kebab":
    print(f"{snack} getting ready ")
else:
    print("Not available")    
