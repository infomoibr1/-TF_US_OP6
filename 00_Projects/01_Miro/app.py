
# Greeting
print("Willkommen bei Miro Restaurant:")
print("=" * 30)


 
# Define the menu
menu = {
    "Pizzen":[
        {"id": 100, "title": "Pizza Margeritta", "price": 5},
        {"id": 101, "title": "Pizza Tunfisch", "price": 5},
        {"id": 102, "title": "Pizza Fungi", "price": 5},
    ],

    "Aufläufe":[
        {"id": 200, "title": "Auflauf Nudeln", "price": 5},
        {"id": 201, "title": "Auflauf Kartoffeln", "price": 5},
        
    ]
    
}


# Show the menu
for category in menu:
    print(category)
    print("=" * 10)

    for dish in menu[category]:
        print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€')


# Get user wishes
print("Wünsche:")
print("=" * 10)

user_wish_list = []

while True:

    user_wish = int(input("> "))

    # exit point
    if user_wish == 0:
        break 

    # Collect the user wishes
    user_wish_list.append(user_wish)


user_wish_list.sort()

# Receipt
print("Rechnung:")
print("=" * 10)

total = 0

for user_wish_id in user_wish_list:  # [100, 102, 201]
    for category in menu:
        for dish in menu[category]:
            if user_wish_id == dish["id"]:  # the ID is found in the menu
                print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€')
                total += dish["price"]

total = round(total , 2)

print(f"Summe : {total} €")

print("Vielen Dank für Ihren Besuch! ")