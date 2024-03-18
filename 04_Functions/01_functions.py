# Without Param
def greeting():
    print("Hallo Mohamed")


# With Single Param
def greeting2(name):
    print("Hallo", name)

# With Multi Param
def greeting3(first_name, last_name):
    print("Hallo", first_name, last_name)

# Param with default value
def greeting4(first_name, last_name, location = "Aachen"):
    print("Hallo", first_name, last_name, location)






greeting()
greeting2("Thomas")

greeting3("Sven", "Meier")


greeting3(last_name= "Meier", first_name="Sven")


greeting4("Frank", "Meier", "Berlin")
greeting4("Sara", "Meier")