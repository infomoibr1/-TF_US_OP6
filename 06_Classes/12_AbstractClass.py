# Abstract Class ::  Class which the consumer CANNOT create an instance from it
# MUST : to have one method decorated as abstract method --> the class will be activated as Abstract class

from abc import ABC , abstractmethod

class Car(ABC):

    company = "WBS"

    def __init__(self, model, kz) -> None:
        self.kz = kz 
        self.model = model

    @abstractmethod
    def process(self):
        pass 

    def fahren(self):
        print("I am driving", self.model)

    @abstractmethod
    def parken(self):
        pass 
   



class VW(Car):
    def __init__(self, model, kz, gps) -> None:
        super().__init__(model, kz)      

        self.gps = gps 

    def gps_start(self):
        print("GPS is started!")

    def process(self):
        print("This is a special process for VW") 


    def parken(self):
        print("I am VW and parking with backwards")

    
class Audi(Car):
    def __init__(self, model, kz, ble) -> None:
        super().__init__(model, kz)
        self.ble = ble 

    def blutooth_start(self):
        print("BLE is started")

    def process(self):
        print("This is a special process for Audi") 
        
    def parken(self):
        print("I am Audi and parking with forwardwards")


# car = Car("asd", "sdf")  #ERRORRR

vw1 = VW("Passat", "AA1234", True)
audi1 = Audi("Passat", "AA1234", True)

vw1.fahren()
vw1.process()
audi1.process()