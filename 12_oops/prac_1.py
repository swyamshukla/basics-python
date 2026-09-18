class Car:
    model=None
    year=None
    def __init__(self,model,year):
        self.model=model
        self.year=year

    def getter(self):
        print(self.model)
        print(self.year)

    def setter(self,model,year):
        self.model

obj=Car('Toyota',2020)


class ElectricCar(Car):
    def __init__(self,model,year,battery_capacity):
        super().__init__(model,year)
        self.battery_capacity=battery_capacity
        

