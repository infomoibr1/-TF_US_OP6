class Car:

    car_counter = 0

    def __init__(self, kz, model) -> None:
        self.kz = kz
        self.model = model 
        Car.car_counter += 1

    def __del__(self):
        Car.car_counter -=1



vw1 = Car("Aa1234", "Passat")
audi1 = Car("BB1234", "Q3")



print(Car.car_counter) # 2


tesla1 = Car("CC1234", "T3")
print(Car.car_counter) # 3

del tesla1 # delete the object from the memory

print(Car.car_counter) # 2