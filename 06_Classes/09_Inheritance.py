class Car:
    def __init__(self, model, kz) -> None:
        self.kz = kz 
        self.model = model



    def fahren(self):
        print("I am driving", self.model)

class ElectricMotor:
    def __init__(self, capa) -> None:
        self.capa = capa

    def electric_motor_start(self):
        print("E Motor start")


# Multi Inheritance
class VW(Car, ElectricMotor):
    def __init__(self, model, kz, gps, capa) -> None:
        super().__init__(model, kz)
        ElectricMotor.__init__(self, capa)

        self.gps = gps 

    def gps_start(self):
        print("GPS is started!")


    
class Audi(Car):
    def __init__(self, model, kz, ble) -> None:
        super().__init__(model, kz)

        self.ble = ble 


    def blutooth_start(self):
        print("BLE is started")




passat = VW("Passat", "Aa12345", True, "2000")
q3 = Audi("Q3", "BB12345", True)


passat.fahren()
q3.fahren()

passat.gps_start()
q3.blutooth_start()


passat.electric_motor_start()