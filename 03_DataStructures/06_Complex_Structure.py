# Access the values

user = { 
        "first_name": "Thomas",  
        "last_name": "Meier", 
        "age": 42,
        "kids": ["Julia", "Paula"],
        "cars": ("VW", "Audi"),
        "kids2": [
            {"id": 100, "first_name": "Julia", "friends": ["Max", "Frank"]},
            {"id": 101, "first_name": "Paula", "friends": ["Juliet", "Dennis" ]}
        ]
    }


print(user["age"])
print(user["last_name"])

print(user["kids"]) # ['Julia', 'Paula']
print(user["kids"][0])

print(user["cars"][1])

print(user["kids2"])

print(user["kids2"][0])
print(user["kids2"][0]["first_name"])

print(user["kids2"][1]["friends"][0])
