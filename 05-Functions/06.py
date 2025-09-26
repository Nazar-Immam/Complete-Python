#TYPES OF FUNCTIONS IN PYTHON


# PURE - doesnt use any global variables

def pure(cups):
    return cups*10

# IMPURE(not recommended) - uses or manipulates the global variables

chaiTotal = 0

def impure(cups):
    global chaiTotal
    chaiTotal += cups


# RECURSIVE FUNCTIONS

def pourchai(n):
    if n ==0 :
        return "All cups poured"
    print(f"Chai poured : {n}")
    pourchai(n-1)

pourchai(4)

# LAMBDA FUNCTIONS(anonymous functions)

chaitypes = ["masala" , "kadak" , "elaichi" , "kadak" , "kadak","oolong" ]

repeated = list( filter( lambda i: i== "kadak" , chaitypes) )

print(repeated)

#to get not kadak 

notkadak = list( filter( lambda i : i!= "kadak" , chaitypes))

print(notkadak)