#Comprehension in dictionary 
#Syntax - { expression(key,value) for item in items if condition}

chai_prices_inr = {
    "Masala Chai" : 40 ,
    "Lemon Tea" : 100 ,
    "Green Tea" : 200 
}

#task - we need to convert all prices into usd 
# means we need to divide every price by 80

prices_in_usd = { tea: price/80  for tea , price in chai_prices_inr.items() }

print(prices_in_usd)