
print("Enter numbers:")
print("=" * 15)


all_numbers = []
pos_numbers = []
neg_numbers = []
total = 0


while True:
    user_input = int(input("> "))

    if user_input == 0: # exit point
        break 
   

    all_numbers.append(user_input)
    total += user_input

    if user_input>0:
        pos_numbers.append(user_input)
    else:
        neg_numbers.append(user_input)


all_numbers.sort()

print("All numbers: ",  all_numbers)
print("POS numbers: ",  pos_numbers)
print("Neg numbers: ",  neg_numbers)


print("Total: ",  total)
print("Min: ",  all_numbers[0])
print("Max: ",  all_numbers[-1])