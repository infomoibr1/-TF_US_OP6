for num in [1, 2, 3, 40, 50]:
    print(num)

for tn in ["Thomas", "Ingo", "Sara", "Lena"]:
    print(tn)



for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num)


""" 
range()
range(10) : 0-9
range(5, 10) : 5 - 9
range(5, 20, 2)  : 5,7,9,...,19
"""

for num in range(5):
    print("Python:", num)

# Ex: Even 10 - 20 
for num in range(10, 21, 2):
    print(num)
print()   

# Ex: Even 10 - 20 (without step)
for num in range(10, 21):
    if num%2 == 0: # even
        print(num)

print()

# Ex: 1 2 3 4 Banana 6 7 8 
for num in range(1, 9):
    if num == 5:
        print("Banana")
    else:
        print(num)



# Nest Loop
        
for char in ["A", "B"]:
    for num in [1,2,3]:
        print(char, num)