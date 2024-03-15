user = { 
        "first_name": "Thomas",  
        "last_name": "Meier", 
        "age": 42,
        "kids": ["Julia", "Paula"],
        "cars": ("VW", "Audi")
    }


print(user, type(user))




# Add 
user["house_nr"] = 6
print(user)


# Edit  a value of a key
user["house_nr"] = 60
print(user)


# Delete key-value pair
user.pop("house_nr")
print(user)


#############################################

for key in user.keys():
    print(key)
print()

for value in user.values():
    print(value)
print()


for item in user.items():
    print(item)
print()


for key in user:
    print(key)