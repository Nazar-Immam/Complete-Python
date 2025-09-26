# break and continue in loop
# break - finishes the loop there only
# continue - skips that iteration

seasons = ["Winter" , "Summer" , "Fall" , "Spring" , "error" , "gajkfds" , "sdaf"]

for i in seasons:
    if i == "Fall":
        continue
    if i == "error":
        break
    print(f"Current season : {i}")