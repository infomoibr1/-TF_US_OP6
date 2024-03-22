""" 
CLass Methods:
1. Different ways to create instances 
2. a Method to change a class based attribute 
"""
class Employee:

    bonus = 400

    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

    def correct_format(self):
        self.first_name = Employee.change_case_status(self.first_name)

    @classmethod
    def create_instance_from_string(cls, emp_string):
        first, last = emp_string.split("-")
        return cls(first, last)  # call to the __init__ and return the created instance

    @classmethod
    def create_instace_from_dict(cls, emp_dict):
        first, last = emp_dict["fn"] , emp_dict["ln"]
        return cls(first, last)  # call to the __init__ and return the created instance

    
    @classmethod
    def set_bonus(cls, new_bonus):
        if new_bonus > 0:
            cls.bonus = new_bonus

    @staticmethod
    def change_case_status(name:str):
        return name.strip().upper()


# 1. TO Provide several ways to create instance
emp1 = Employee("Thomas", "Meier") # 1. way: classical constructor

emp2 = Employee.create_instance_from_string("Sven-Meier") # 2. create instance via another way --> class method

emp3 = Employee.create_instace_from_dict({"fn": "Lena", "ln": "Meier"}) # 3. way: create instance via Dict --> class method

print(emp1)
print(emp2)
print(emp3)


# 2. To change a Class based attribute via a Method (validation ,etc.)
print(Employee.bonus) # 400



Employee.set_bonus(-600)

print(Employee.bonus) # 400  --> -600 wurde abgelehnt

# NOT Recommened but works -> you can change the class based attribute via the instance
emp1.set_bonus(800)

print(Employee.bonus) # 800
print(emp2.bonus)



# ====================================================
# Static Methods: methods with do not belong to class or instance
# Static Methods: does not have access to attributes
# Static Methods: the consumer can also use them without creating an instance
emp1.correct_format()
print(emp1)

result = Employee.change_case_status("Apfel")
print(result)

 