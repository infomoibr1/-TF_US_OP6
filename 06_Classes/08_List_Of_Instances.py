class Company:

    def __init__(self) -> None:        
        self.list_of_employees = []



class Employee:
    pass 



# Company
wbs = Company()

# MA
thomas = Employee()
sven = Employee()


# Add the EMployee to the company
wbs.list_of_employees.append(thomas)
wbs.list_of_employees.append(sven)



for emp in wbs.list_of_employees:
    print(emp)