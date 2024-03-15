numbers = [1, 2,3,4,5]
print(numbers, type(numbers))

teilnehmende =["Thomas", "Ingo", "Sara", "Lena", "Julia"]
print(teilnehmende)


mixed_data= ["Thomas", 12 , True, 15.4]
print(mixed_data)


zeros = [0] * 20
print(zeros)


matrix = [[1,2] , [3,4]]
print(matrix)

empty_list = [] # empty list


##############################################
# access items
teilnehmende = ["Thomas", "Ingo", "Sara", "Lena", "Julia"]

print(teilnehmende)
print(teilnehmende[0])
print(teilnehmende[-1])
print(teilnehmende[0:3])
print(teilnehmende[3:])
print(teilnehmende[3:5])
print(teilnehmende[-2:-1])
print(teilnehmende[-2:0])
print(teilnehmende[-2:])


print(teilnehmende[0:5:2]) # step 2
print()

################################################
teilnehmende = ["Thomas", "Ingo", "Sara", "Lena", "Julia"]


counter = 1

for tn in teilnehmende:    
    print(f"{counter}. {tn}")
    counter += 1

"""
1. Thomas
2. Ingo
3. Sara
4. Lena
5. Julia
"""
print() 


# Alternative
for tn in enumerate(teilnehmende):   # (0, 'Thomas')
    print(tn[0], tn[1])


# Unpacking
for idx, name in enumerate(teilnehmende):
    print(idx, name)


############################################################  