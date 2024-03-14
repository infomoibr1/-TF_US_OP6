temperature = 5 


if temperature >= 30:
    print("Es ist heiß")
elif temperature >= 20:
    print("Es ist warm")

elif temperature >= 10:
    print("Es ist cool")
else:
    print("Es ist kalt")


# Nested if: Online Shop 
age = 25 
payment_method = False 

if age>=18:
    if payment_method == True:
        print("Zur Kasse bitte")
    else:
        print("Du muss BZ-Method eingeben")

else:
    print("Du bist zu jung")