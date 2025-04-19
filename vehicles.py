class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def move(self):
        print("Flying ✈️")