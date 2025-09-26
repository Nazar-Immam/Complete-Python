#Dictionary in place of Match- case

users = [
    {"id" : 1 , "total" : 100 , "coupun code" : "NS12" },
    {"id" : 2 , "total" : 120 , "coupun code" : "GS12" },
    {"id" : 3 , "total" : 200 , "coupun code" : "NY12" },
]

#Now according to the coupun codes we need to give the discounts to the user
#For this we can use dictionary

discounts = {
    "NS12" : (0.2,0),
    "GS12" : (0.5,0),
    "NK12" : (1, 10),
}

for user in users :
    percent ,fixed  = discounts.get(user["coupun code"] , (0,0))
    discount = user["total"] * percent + fixed 
    print(f"Disount got is : {discount}")

