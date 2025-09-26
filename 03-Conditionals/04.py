device_status = 'active'
temp = 36

if device_status == 'active' :
    if temp > 35 :
        print("Warning ! High Temperature")
    else:
        print("Temperature Normal") 
else:
    print("Device Off")           
