
location = "Berlin"

def greeting1(name):
    print("Hallo,", name)
    x = 10 
    print(x)


def greeting2(name):
    print("Hallo,", name)
    print(location) # read GLobal variable 


def greeting3(name):
    print("Hallo,", name)

    location = "Frankfurt" # creates a LOCAL variable
    
    print(location) # Frankfurt



def greeting4(name):
    global location # makes the global variable changeable 

    print("Hallo,", name)

    location = "Aachen" #  changes the global value

    print(location) # Aachen





greeting1("Thomas")
greeting2("Sven")
greeting3("Sara")


print(location) # Berlin

greeting4("Lena")
print(location) # Aachen


print("Ende")