# special
#for - else 

staff = [ ("Amit" , 15) ,("Sumit" , 17) ,("Raj" , 16) ,("John" , 13) ]

for names, age in staff:
    if age >16 :
        print(f"{names} is eligible for the job ")
        break
else:
    print("All are underage")

# ELSE ONLY WORKS IF THE LOOP DID'NT BREAK
# Mtlb pura loop chal gaya uske baad else hit hota hai, agar kahin break hit hogaya to else nhi chalega