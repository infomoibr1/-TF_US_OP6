class Employee:

    bonus = 500  # Class Based Attribute

    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 


    def show_info(self):
        print(f"{self.first_name} - {self.last_name}")


# create instances
thomas = Employee("Thomas", "Meier")
sven = Employee("Sven", "Meier")


print(thomas.__dict__) # {'first_name': 'Thomas', 'last_name': 'Meier'}
print(sven.__dict__) # {'first_name': 'Sven', 'last_name': 'Meier'}


print(thomas.bonus)
print(sven.bonus)


###################################################

# Special Condition for Thomas
thomas.bonus = 700

print(thomas.bonus)
print(sven.bonus)

print(thomas.__dict__) # {'first_name': 'Thomas', 'last_name': 'Meier', 'bonus': 700}
print(sven.__dict__)   # {'first_name': 'Sven', 'last_name': 'Meier'}
#############################

# Change the Class Attribute value
Employee.bonus = 1200 


print(thomas.bonus)
print(sven.bonus)


print(thomas.__dict__) # {'first_name': 'Thomas', 'last_name': 'Meier', 'bonus': 700}
print(sven.__dict__)   # {'first_name': 'Sven', 'last_name': 'Meier'}