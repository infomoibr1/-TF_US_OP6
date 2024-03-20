class Car:

    def __init__(self, model, bj, color) -> None:
        self.model = model 
        self.bj = bj
        self.color = color 
        self.km_stand = 0


    def drive(self, km):
        self.km_stand += km

    def show_info(self):
        print(f"{self.model} - KM: {self.km_stand}")



vw1 = Car("VW Passat", 2023, "Black")
vw2 = Car("VW Passat", 2023, "Red")


vw1.drive(200)
vw1.drive(300)
vw1.drive(300)

vw2.drive(300)


vw1.show_info()
vw2.show_info()
       


 