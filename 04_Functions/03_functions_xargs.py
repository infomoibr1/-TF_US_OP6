
# X-Arguments: beliebiger Anzahl von Arguments 

# *container: Tuple --> sammelt alle values drin

def add(*xargs):

    total = sum(xargs)

    print(total)



add(10,20)
add(10,20,30)
add(10,20,30, 40)