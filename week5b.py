# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  # Generic method

# Derived classes with unique move() behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛴️")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for v in vehicles:
    v.move()
