
# Define a string
course_name = "Python"
course_name = 'Python'


print(course_name)


# Multi-Line String
message = """Hallo Mohamed
wie geht es dir ?
schöne Grüße
Tobias"""


print(message)



# len()
course_name = "Python"
print(len(course_name))


# Slicing
course_name = "Einführung in Python"
print(course_name)
print(course_name[0])
print(course_name[14])
print(course_name[-6])
print(course_name[0:9]) # Einführun
print(course_name[0:10]) # Einführung
print(course_name[14:20]) # 
print(course_name[14:21]) # 
print(course_name[14:22]) # 

print(course_name[14:2000]) # 

print(course_name[14:]) # bis Ende
print(course_name[:10]) # vom Anfang

print(course_name[:]) # complete
print(course_name) 


# String Methods : DOT Function
###################


course_name = "    einFührunG in pyThoN  "

print(course_name)
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.strip())

print(course_name.find("py"))  # 18: index where py starts
print(course_name.find("jy")) # -1: not found

print(course_name.replace("py", "jy"))
print(course_name.split())


# Method Chain

course_name = course_name.upper() 
course_name = course_name.strip()
print(course_name)


course_name  = course_name.title().strip()
print(course_name)




###########################################
# Ignoring/Escaping Charachter  \
# \n: NewLine
# \t: TAB

# Mohamed sagte "Guten Morgen" heute
# Mohamed sagte 'Guten Morgen' heute
# Mohamed sagte \Guten Morgen\ heute

print("Mohamed sagte \"Guten Morgen\" heute")

print('Mohamed sagte \'Guten Morgen\' heute')

print("Mohamed sagte \\Guten Morgen\\ heute")

print('Mohamed sagte "Guten Morgen" heute')
print("Mohamed sagte 'Guten Morgen' heute")

print("Python\nJava")
print("Python\tJava")


###################################
# string concatenation

first_name  = "Thomas"
last_name = "Meier"

print(first_name +   last_name)

full_name = first_name + " " + last_name
print(full_name)


# String formating
full_name = "{} {}".format(first_name, last_name)
print(full_name)


full_name = f"{first_name} {last_name}" 
print(full_name)


full_name = f"First Name: {first_name} - Last Name: {last_name}" 
print(full_name)


