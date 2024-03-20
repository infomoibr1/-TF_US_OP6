# self : Instance based  attribute / method

class Employee:
    
    def __init__(self, first_name, last_name, location = None):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.salary = 0
        self.plz = ""
        

    def show_my_name(self) :
       print("My Name is:", self.first_name)

    def show_all_info(self):
        print(f"FN: {self.first_name} - LN: {self.last_name} - Salary: {self.salary} - Location : {self.location}")
 

# Create instances
thomas = Employee("Thomas", "Meier")
sven = Employee("Sven", "Meier")
sara = Employee("Sara", "Meier", "Aachen")


thomas.show_my_name()
sven.show_my_name()

thomas.salary = 5000
sven.salary = 7000

thomas.show_all_info()
sven.show_all_info()
sara.show_all_info()

thomas.plz = 12345


employee_list = [thomas, sven, sara]

for emp in employee_list:
    print(emp.first_name,  emp.last_name, emp.salary, emp.plz  )



 
 
