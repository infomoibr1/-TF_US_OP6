# Pure Private attributes are NOT in Python
# __private (2 underscores)

class Employee:

    __company = "WBS"

    def __init__(self, first_name, last_name, salary, bonus) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary # public
        self.bonus = bonus
        self.project_list = []

   
    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.__salary}"

    def show_info(self):
        print(f"{self.first_name} {self.last_name} {self.__salary}")

   

# Consumer
        
thomas = Employee("Thomas", "Meier", 5000 , 7000)
sven = Employee("Sven", "Meier", 5000 , 3000)


print(thomas.first_name)
print(thomas._Employee__salary) # 5000

# Change the private attribute
thomas._Employee__salary = 4000

print(thomas._Employee__salary)


print(Employee._Employee__company)

# Change the Class based attribute
Employee._Employee__company = "WBS Training"

print(Employee._Employee__company)

