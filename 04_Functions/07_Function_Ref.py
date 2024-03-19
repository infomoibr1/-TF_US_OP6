
def greeting1(name):
    print("Hallo,", name)


greeting1("Thomas")


print(  greeting1    ) #  The address <function greeting1 at 0x000002D026BD04A0>

greeting1("Sven") ## Call the address



#########################################################

def greeting1(name):
    print("Hallo,", name)
    return 10 

# Call the function
result = greeting1("Thomas")
print(result)  # 10


# 
result = greeting1
print(result)  # <function greeting1 at 0x000001F3B77B8B80>

result("Lena") # It is a CALL of the address --> Call of the greeting1()


