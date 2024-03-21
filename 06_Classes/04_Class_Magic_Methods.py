# Magic Methods / Dunder Methods

class Employee:

    def __init__(self, first_name, last_name, salary, bonus) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary 
        self.bonus = bonus
        self.project_list = []

    def __eq__(self, other):  # __eq__ : equal ==
        return self.salary == other.salary
    

    def __gt__(self, other):
        return self.bonus > other.bonus
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.salary}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.salary}"

    def __len__(self):
        return len(self.project_list)
    
    def __add__(self, other):
        return self.salary + other.salary

    def show_info(self):
        print(f"{self.first_name} {self.last_name} {self.salary}")

   

thomas = Employee("Thomas", "Meier", 5000 , 7000)
sven = Employee("Sven", "Meier", 5000 , 3000)


print(thomas == sven)
print(thomas > sven)
print(thomas < sven)


print(thomas.salary)


thomas.show_info() # classical way

print(thomas)

thomas.project_list.append("Project A")
thomas.project_list.append("Project B")

print(len(thomas))




print(thomas + sven)

 