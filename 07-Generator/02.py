#Infinte generators

def infiniteChai():
    count = 1 

    while True:
        yield f"Refil #{count}"
        count += 1 

refillcups = infiniteChai()

for _ in range(5):
    print(next(refillcups))


user2 = infiniteChai()

for _ in range(2):
    print(next(user2))