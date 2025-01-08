class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Model: {self.model}, make: {self.make}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
       return f"Model: {self.model}, make: {self.make}, fuel type: {self.fuel_type}"

c = Car(1,2,3)
print(c.get_info())
