#When we know some of our code can give error, then we use special method for custom error, 
#and also by which the entire code doesn't get stopped
# try except

chai_menu = {"masala": 30 , "ginger":40}
#print(chai_menu["elaichi"])  // this would give error as we accessing the key which is not present, ie KeyError

try:
    print(chai_menu["elaichi"])
except:
    print("The key you entered does not exist. ")


print("Hello World !")